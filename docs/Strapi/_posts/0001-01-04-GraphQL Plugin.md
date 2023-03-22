---
title: GraphQL Plugin
layout: docs
permalink: /:categories/:title/
---


# Usage

下載graphql套件到strapi project
`yarn strapi install graphql`

playground網址預設在/graphql
>graphql playground [http://localhost:1337/graphql](http://localhost:1337/graphql)

# Config

*set playgroundAlways: true at config/plugins.ts*

```ts
# config/plugins.ts
export default {
  //
  graphql: {
    config: {
      endpoint: '/graphql',
      shadowCRUD: true,
      playgroundAlways: false,
      depthLimit: 7,
      amountLimit: 100,
      apolloServer: {
        tracing: false,
      },
    },
  },
};
```

# Shadow CRUD

Shadow CRUD會根據model自動生成(type definitions, queries, mutations and resolvers)，在playground有docs可以參考


# Customization

Strapi provides a programmatic API to customize GraphQL, which allows:
1.  disabling some operations for the Shadow CRUD
2. [using getters](https://docs.strapi.io/dev-docs/plugins/graphql#using-getters) to return information about allowed operations
3. registering and using an `extension` object to [extend the existing schema](https://docs.strapi.io/dev-docs/plugins/graphql#extending-the-schema) (e.g. extend types or define custom resolvers, policies and middlewares)

## Example

客製化的內容加在src/index.ts的register中才會生效
目前已知有兩種方法可以擴充graphql

1.  [Nexus](https://nexusjs.org/)-based type definitions (官方好像叫推薦這個)
2.  [GraphQL SDL](https://graphql.org/learn/schema/)

```ts
./src/index.ts
export default {
  /**
   * An asynchronous register function that runs before
   * your application is initialized.
   *
   * This gives you an opportunity to extend code.
   */
  register({ strapi }) {
    const extensionService = strapi.plugin('graphql').service('extension');
    
	  // 關閉shadow crud某些api
    extensionService.shadowCRUD('api::restaurant.restaurant').disable();
    extensionService.shadowCRUD('api::category.category').disableQueries();
    extensionService.shadowCRUD('api::address.address').disableMutations();
    extensionService.shadowCRUD('api::document.document').field('locked').disable();
    extensionService.shadowCRUD('api::like.like').disableActions(['create', 'update', 'delete']);
    
    const extension = ({ nexus }) => ({
      // Nexus (新增object、擴充object、新增query)
      types: [
		// 新增object book，含有field title
        nexus.objectType(Creator),
		// extend exist object type
		nexus.extendType(extendProduct),
		// 新增query
		nexus.extendType(getproductsByCreatorId),
      ],
      // qeury不驗證的話要在這裡把auth改成false
      resolversConfig: {
        'Query.address': {
          auth: false,
        },
      },
    });
	// 加載設定
    extensionService.use(extension);
  },
};
```


##  Nexus-based type definitions

### Object Type
```ts
// new object
const Creator = {
  type: 'Creator',
  name: 'Creator',
  definition(t) {
    t.int('id');
    t.string('firstname');
    t.string('lastname');
    t.string('username');
  }
}
```
### Extend Object Type
```ts
//Extend exist object type
const extendProduct = {
  type: 'Product',
  definition(t) {
    // we want to know who is the creator
    t.field('createdBy', {
      type: 'Creator',
      async resolve(root, args, ctx) {
        // when we use query, we can populate createdBy
        const query = strapi.db.query('api::product.product');
        const product = await query.findOne({
          where: {
            id: root.id,
          },
          populate: ['createdBy'],
        });
        return {
          id: product.createdBy.id,
          firstname: product.createdBy.firstname,
          lastname: product.createdBy.lastname,
          username: product.createdBy.username
        };
      },
    })
  }
}
```

### Query
```ts
//New query
const getproductsByCreatorId = {
  type: 'Query',
  definition(t) {
    //  productsByCreatorId definition
    t.field('getProductsByCreatorId', {
      // Response type
      type: list('Product'),
      // Argument
      args: { id: idArg() },
      // Resolver definition: Filte products by createdById
      async resolve(root, args, ctx) {
        
        const query = strapi.db.query('api::product.product');
        const product = await query.findMany({
          populate: ['createdBy'],
          where: {
            $and: [
              {
                createdBy: {
                  id: args.id
                }
              },
              {
	            // caution: this will return only published data but draft!
                $not: {
                  publishedAt: null
                }
              }
            ]
          }
        });
        return product;
      }
    });
  }
}
```
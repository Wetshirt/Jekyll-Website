---
title: Upload(Media Library)
layout: docs
permalink: /:categories/:title/
---

# Intro

>The Upload plugin is the backend powering the Media Library plugin available by default in the Strapi admin panel.
>
>By default Strapi provides a [provider](https://docs.strapi.io/dev-docs/providers) that uploads files to a local directory. Additional providers are available should you want to upload your files to another location.

The providers maintained by Strapi include:
-   [Amazon S3](https://market.strapi.io/providers/@strapi-provider-upload-aws-s3)
-   [Cloudinary](https://market.strapi.io/providers/@strapi-provider-upload-cloudinary)
-   [Local](https://www.npmjs.com/package/@strapi/provider-upload-local)

# Local

## Configuration

By default Strapi accepts `localServer` configurations for locally uploaded files. These will be passed as the options for [koa-static](https://github.com/koajs/static).

You can provide them by creating or editing the `./config/plugins.js` file. The following example sets the `max-age` header.

```javascript
//./config/plugins.js
module.exports = ({ env })=>({  
	upload: {  
		config: {  
			providerOptions: {  
				localServer: {  
					maxage: 300000  
				},  
			},  
		},  
	},  
});
```


### Max file size


> Currently the Strapi middleware in charge of parsing requests needs to be configured to support file sizes larger than the default of 200MB in addition to provider options passed to the upload plugin for sizeLimit.

**預設上傳大小為200MB**，可以在`./config/middlewares.js`設定

```javascript
module.exports = [
  // ...
  {
    name: "strapi::body",
    config: {
      formLimit: "256mb", // modify form body
      jsonLimit: "256mb", // modify JSON body
      textLimit: "256mb", // modify text body
      formidable: {
        maxFileSize: 250 * 1024 * 1024, // multipart data, modify here limit of uploaded file size
      },
    },
  },
  // ...
];
```

### Responsive Images (TBC)

## Endpoint

| Method | Path | Description |
|--------|------|-------------|
|GET|/api/upload/files|Get a list of files|
|GET|/api/upload/files/:id|Get a specific file|
|POST|/api/upload|Upload files|
|POST|api/upload?id=x|Update fileInfo|
|DELETE|/api/upload/files/:id|Delete a file|

## Examples
(tbc)


# AWS S3

## Intro
(tbc)


## Install Providers

```shell
#Install the AWS S3 provider for the Upload plugin

yarn add @strapi/provider-upload-aws-s3

# Install the Sendgrid provider for the Email plugin
yarn add @strapi/provider-email-sendgrid --save

```

## Configuration

### Plugin

./config下新增plugins.js

```ts
// config/plugins.ts 
export default ({ env }) => ({
    upload: {
      config: {
        provider: 'aws-s3',
        providerOptions: {
          accessKeyId: env('AWS_ACCESS_KEY_ID'),
          secretAccessKey: env('AWS_ACCESS_SECRET'),
          region: env('AWS_REGION'),
          params: {
            Bucket: env('AWS_BUCKET'),
          },
        },
        actionOptions: {
          upload: {},
          uploadStream: {},
          delete: {},
        },
      },
    },
});
```

### Middleware

>Due to the default settings in the Strapi Security Middleware, you will need to modify the `contentSecurityPolicy` settings to properly see thumbnail previews in the Media Library.

要讀取到預覽圖(thumbnail previews)需設定middleware，修改`./config/middleware.ts`並設定bucket name、region

```ts
export default [
  'strapi::errors',
  
  /* Replace 'strapi::security', with this snippet */
  /* Beginning of snippet */
  {
    name: 'strapi::security',
    config: {
      contentSecurityPolicy: {
        useDefaults: true,
        directives: {
          'connect-src': ["'self'", 'https:'],
          'img-src': [
            "'self'",
            'data:',
            'blob:',
            'dl.airtable.com',
            'yourBucketName.s3.yourRegion.amazonaws.com',
          ],
          'media-src': [
            "'self'",
            'data:',
            'blob:',
            'dl.airtable.com',
            'yourBucketName.s3.yourRegion.amazonaws.com',
          ],
          upgradeInsecureRequests: null,
        },
      },
    },
  },
  /* End of snippet */
  
  'strapi::cors',
  'strapi::poweredBy',
  'strapi::logger',
  'strapi::query',
  'strapi::body',
  'strapi::session',
  'strapi::favicon',
  'strapi::public',
];

```

### env

.env新增aws變數，Access Key ID、Secret access key在[[#Set Up AWS]]建立使用者後取得

```
# AWS S3
AWS_ACCESS_KEY_ID=<Access Key ID>
AWS_ACCESS_SECRET=<Secret access key>

# eu-west-2
AWS_REGION=<regipon>

# strapi-aws-s3-images-bucket
AWS_BUCKET=<bucket-name>
```



## Set Up AWS

### User

(TBC)
目前是直接使用root user的金鑰(不建議)，未來要新增IAM使用者並給予S3權限

### Bucket

- object owner -> ACLs: enabled (未來重構api應可解決) -> object ownership: **Bucket owner preferred**
- Under **Block Public Access settings for this bucket** -> Uncheck **Block all public access**



# References
https://docs.strapi.io/dev-docs/plugins/upload#max-file-size
https://strapi.io/blog/how-to-set-up-amazon-s3-upload-provider-plugin-for-our-strapi-app





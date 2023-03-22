---
title: Admin Panel Customization
layout: docs
permalink: /:categories/:title/
---

# Customization options

## [access URL, host and port](https://docs.strapi.io/dev-docs/admin-panel-customization#access-url)

修改網址如下
> ex. `http://localhost:8888/dashboard`

修改port
```
# ./config/server.ts
export default ({ env }) => ({  
	host: env('HOST', '0.0.0.0'),  
	port: env.int('PORT', 8888),  
});
```

修改URL
```
# ./config/admin.ts
export default ({ env }) => ({  
	url: '/dashboard',  
})
```

## [Configuration options](https://docs.strapi.io/dev-docs/admin-panel-customization#configuration-options)

### [Locales](https://docs.strapi.io/dev-docs/admin-panel-customization#locales)
後台管理的語言可以選擇(User Profile->Experience)
```
# ./src/admin/app.ts
export default {  
	config: {  
		locales: ['ru', 'zh']  
	},  
	bootstrap() {},  
}
```
需使用`yarn build`才會更新UI Panel
### [Logos](https://docs.strapi.io/dev-docs/admin-panel-customization#logos)
### [Favicon](https://docs.strapi.io/dev-docs/admin-panel-customization#favicon)



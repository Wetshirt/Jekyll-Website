---
title: Providers
layout: docs
permalink: /:categories/:title/
---


Certain [plugins](https://docs.strapi.io/user-docs/plugins) can be extended via the installation and configuration of additional [providers](https://docs.strapi.io/user-docs/plugins#providers).

Providers add an extension to the core capabilities of the plugin, for example to upload media files to AWS S3 instead of the local server, or using Amazon SES for emails instead of Sendmail.

>Only the [Upload](https://docs.strapi.io/dev-docs/plugins/upload) and [Email](https://docs.strapi.io/dev-docs/plugins/email) plugins are currently designed to work with providers.

# Upload 

官方支援的plugin已有教學[[99. Upload(Media Library)#AWS S3]]


## Creating providers

To implement your own custom provider you must [create a Node.js module](https://docs.npmjs.com/creating-node-js-modules).

### 1. Create a `package.json` file

- npm init
- 自動產生package.json並設定相關資訊

```json
# package.json
{
  "name": "test-module",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

### 2.  Develop provider

```ts
export default {
  init(providerOptions) {
    // init your provider if necessary

    return {
      upload(file) {
        // upload the file in the provider
        // file content is accessible by `file.buffer`
      },
      uploadStream(file) {
        // upload the file in the provider
        // file content is accessible by `file.stream`
      },
      delete(file) {
        // delete the file in the provider
      },
    };
  },
};
```

- providerOptions that contains configurations written in plugins.js
- settings that contains configurations written in plugins.js
- options that contains options you send when you call the send function from the email plugin service
#### Example Provider

- [AWS S3](https://github.com/strapi/strapi/tree/main/packages/providers/upload-aws-s3)
- [Local](https://github.com/strapi/strapi/tree/main/packages/providers/upload-local)


### 3. npm install

1. Create a `providers` folder under root application
2. Create your provider (e.g. `./providers/strapi-provider-upload-<provider>`)
3. Edit package.json under root application to link provider
```json
{
  ...
  "dependencies": {
    ...
    "strapi-provider-<plugin>-<provider>": "file:providers/strapi-provider-<plugin>-<provider>",
    ...
  }
}
```

4. Update your `./config/plugins.js` file to [configure the provider](https://docs.strapi.io/dev-docs/providers#configuring-providers).
5. run `yarn install` or `npm install`

# Email


(TBC)

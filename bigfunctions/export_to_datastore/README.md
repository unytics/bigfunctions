---
title: "export_to_datastore"
description: "BigFunction export_to_datastore: Exports `data` to Datastore
(Firestore in Datastore mode).

(💡 *For this to work, `749389685934-compute@developer.gserviceaccount.com` must have datastore user role in your project.*)

| Param       | Possible values  |
|-------------|---|
| `project`   | Google Cloud project hosting the Datastore data. Should be unique for one query  |
| `namespace` | A namespace is like a dataset / a folder. It has many `kinds` which are like tables. If `namespace`is `null`, `default` namespace will be used. |
| `kind`      | `kind` is like a table: a set of similar objects. Cannot be `null`. |
| `key`       | Unique identifier where `data` is stored inside `kind`. Can be an integer represented as a string (`key` is then named `id` in Datastore) or any string (`key` is named `name` in Datastore). If `null` a integer key (represented as string) will be generated. |
| `data`      | A json dict of data  |
"
---

<span style="color: silver; position: relative; top: -1rem">
  <a href=".." style="color: silver">bigfunctions </a> > export_to_datastore
</span>

# export_to_datastore


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/el-walid/" title="Author: El-Walid" target="_blank">
    <img src="https://media.licdn.com/dms/image/C4E03AQH6oIAxScy4gw/profile-displayphoto-shrink_800_800/0/1654708759415?e=1691625600&v=beta&t=U6Tgwl4JWamN4qYDJP2b498aJt5thWog84-qnbkz0bU" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="{REPO_URL}/tree/main/bigfunctions/export_to_datastore.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
export_to_datastore(project, namespace, kind, key, data)
```

**Description**

Exports `data` to Datastore
(Firestore in Datastore mode).

(💡 *For this to work, `749389685934-compute@developer.gserviceaccount.com` must have datastore user role in your project.*)

| Param       | Possible values  |
|-------------|---|
| `project`   | Google Cloud project hosting the Datastore data. Should be unique for one query  |
| `namespace` | A namespace is like a dataset / a folder. It has many `kinds` which are like tables. If `namespace`is `null`, `default` namespace will be used. |
| `kind`      | `kind` is like a table: a set of similar objects. Cannot be `null`. |
| `key`       | Unique identifier where `data` is stored inside `kind`. Can be an integer represented as a string (`key` is then named `id` in Datastore) or any string (`key` is named `name` in Datastore). If `null` a integer key (represented as string) will be generated. |
| `data`      | A json dict of data  |






**Examples**



<span style="color: var(--md-typeset-a-color);">1. Export `data` to default namespace with auto-generated `key`.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.export_to_datastore('your-project', null, 'user', null, json '{"name": "Marc Harris", "email": "marc@harris.com"}')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.export_to_datastore('your-project', null, 'user', null, json '{"name": "Marc Harris", "email": "marc@harris.com"}')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.export_to_datastore('your-project', null, 'user', null, json '{"name": "Marc Harris", "email": "marc@harris.com"}')
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+------------------+
| key              |
+------------------+
| 4503604769587200 |
+------------------+
</code>
</pre>









<span style="color: var(--md-typeset-a-color);">2. Export `data` to default namespace, with email as `key`.</span>









=== "EU"

    ```sql
    select bigfunctions.eu.export_to_datastore('your-project', null, 'user', 'marc@harris.com', json '{"name": "Marc Harris"}')
    
    ```




=== "US"

    ```sql
    select bigfunctions.us.export_to_datastore('your-project', null, 'user', 'marc@harris.com', json '{"name": "Marc Harris"}')
    
    ```




=== "europe-west1"

    ```sql
    select bigfunctions.europe_west1.export_to_datastore('your-project', null, 'user', 'marc@harris.com', json '{"name": "Marc Harris"}')
    
    ```









<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">+-----------------+
| key             |
+-----------------+
| marc@harris.com |
+-----------------+
</code>
</pre>










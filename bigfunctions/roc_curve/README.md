---
title: "roc_curve"
description: "BigFunction roc_curve: Returns the Receiver Operating Characteristic Curve (a.k.a. ROC Curve)
given a set of predicted scores and ground truth labels"
---

<a style="color: gray; position: relative; top: -1rem" href="..">BigFunctions </a> / 

# roc_curve


<div style="position: relative; top: -4rem; margin-bottom:  -2rem; text-align: right; z-index: 9999;">
  
  <a href="https://www.linkedin.com/in/anatolec/" title="Author: Anatole Callies" target="_blank">
    <img src="https://ca.slack-edge.com/T01LGTNUWTE-U044NKG25GX-7469e33feefb-512" width="32" style=" border-radius: 50% !important">
  </a>
  
  <a href="roc_curve.yaml" title="Edit on GitHub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#5d6cc0" d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
</div>



**Signature** 
```
roc_curve(predictions)
```

**Description**

Returns the Receiver Operating Characteristic Curve (a.k.a. ROC Curve)
given a set of predicted scores and ground truth labels





**Examples**













=== "EU"

    ```sql
    select * from bigfunctions.eu.roc_curve([(0.1, false), (0.4, false), (0.35, true), (0.8, true)])
    
    ```




=== "US"

    ```sql
    select * from bigfunctions.us.roc_curve([(0.1, false), (0.4, false), (0.35, true), (0.8, true)])
    
    ```




=== "europe-west1"

    ```sql
    select * from bigfunctions.europe_west1.roc_curve([(0.1, false), (0.4, false), (0.35, true), (0.8, true)])
    
    ```











<pre style="margin-top: -1rem;">
<code style="padding-top: 0px; padding-bottom: 0px;">
+---------------------+--------------------+
| false_positive_rate | true_positive_rate |
+---------------------+--------------------+
|         0.0         |         0.0        |
|         0.0         |         0.5        |
|         0.5         |         0.5        |
|         0.5         |         1.0        |
|         1.0         |         1.0        |
+---------------------+--------------------+

</code>
</pre>








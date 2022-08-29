![logo_and_name](https://user-images.githubusercontent.com/111615732/186508787-6af04ed0-4750-4c49-926a-eacfd4a3dfbb.png)
<p align="center">
    <em>Open BigQuery Functions, SQL Superpowers, DataWarehouse in the middle</em>
</p>

---

**Documentation**: <a href="https://unytics.github.io/bigfunctions/" target="_blank">[https://unytics.github.io/bigfunctions/](https://unytics.github.io/bigfunctions/)</a>

---

BigFunctions are open BigQuery routines that give you new *SQL powers* in BigQuery 💪.


```sh
git clone "https://github.com/unytics/bigfunctions"
pip install pyyaml
python scripts/deploy_js_libs.py --generate-js-libs-package-json
npm install
python scripts/deploy_js_libs.py --generate-webpack-configs
npm run-script build-all-libs
gsutil cp js_builds/* gs://bigfunctions_js_libs/

```
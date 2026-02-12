# SHACL Changelog
Este archivo registra todos los cambios significativos en los archivos SHACL de DCAT-AP-ES.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

## Febrero 2026
### Fixes
- flexibilizar la convención 12 en SHACL (Convención 12) - `shacl_dataset_hvd_shape.ttl` ([`fbe59eb`](https://github.com/datosgobes/DCAT-AP-ES/commit/fbe59eb2c273101f768fddb7575d1851f81c2ac2)) - [@mjanez](https://github.com/mjanez)

---

## Febrero 2026
### Features
- añadir gestión automatizada de changelog de formas SHACL - `CHANGELOG.md`, `README.md` ([`7205ca7`](https://github.com/datosgobes/DCAT-AP-ES/commit/7205ca778acb6786cdee51b8eab77c1f2511ea2f)) - [@mjanez](https://github.com/mjanez)
- incluir mensajes de validación y enlaces para convenciones de fecha en las formas SHACL - `shacl_catalog_shape.ttl`, `shacl_dataset_shape.ttl`, `shacl_distribution_shape.ttl` ([`de4faf8`](https://github.com/datosgobes/DCAT-AP-ES/commit/de4faf85610f388911c7e9c89ac1450d44390437)) - [@mjanez](https://github.com/mjanez)
- mejorar mensajes de validación para vcard:Kind en las restricciones SHACL - `shacl_common_shapes.ttl` ([`de009e8`](https://github.com/datosgobes/DCAT-AP-ES/commit/de009e85e9a5b12e61b0ceb416dd122b98fca5f5)) - [@mjanez](https://github.com/mjanez)

### Fixes
- corregir nombre de variables en consultas SPARQL - `shacl_dataset_shape.ttl`, `shacl_distribution_shape.ttl` ([`80806c8`](https://github.com/datosgobes/DCAT-AP-ES/commit/80806c883fe51bf5fec0a222cf4aa0b6b9987a9f)) - [@mjanez](https://github.com/mjanez)
- alinear mensajes de validación para vcard:Kind en las restricciones SHACL - `shacl_common_shapes.ttl` ([`582ee6f`](https://github.com/datosgobes/DCAT-AP-ES/commit/582ee6f79c3ada603fbcb7fc1a8ae5929dc9b876)) - [@mjanez](https://github.com/mjanez)
- ajustar restricción de decimal en propiedades time:* en vez de nonNegativeInteger - `shacl_common_shapes.ttl`, `shacl_dataset_shape.ttl` ([`d8547a0`](https://github.com/datosgobes/DCAT-AP-ES/commit/d8547a045dc188db3668f3ffc9c4907369ad85ea)) - [@mjanez](https://github.com/mjanez)
- agregar mensajes de validación y enlaces para las vcardKind globables - `shacl_dataservice_shape.ttl`, `shacl_dataset_shape.ttl` ([`96c620d`](https://github.com/datosgobes/DCAT-AP-ES/commit/96c620d8bff4c00a16ed16735654c5239bceca90)) - [@mjanez](https://github.com/mjanez)
- mejorar mensajes de validación para DurationDescription_Shape - `shacl_common_shapes.ttl`, `shacl_dataset_shape.ttl` ([`3a70e17`](https://github.com/datosgobes/DCAT-AP-ES/commit/3a70e170618a82696dffc1b518a842703968a7ca)) - [@mjanez](https://github.com/mjanez)

### Refactoring
- simplificar los prefijos del targetSPARQL en Frequency_Shape - `shacl_dataset_shape.ttl` ([`dda3c23`](https://github.com/datosgobes/DCAT-AP-ES/commit/dda3c2363f885423228c224a404e74d89380cd99)) - [@mjanez](https://github.com/mjanez)

### Documentation
- Update SHACL CHANGELOG [automated] - `CHANGELOG.md` ([`398e166`](https://github.com/datosgobes/DCAT-AP-ES/commit/398e1661aefbae55d492930193f0f21bdfdb66eb)) - [@github-actions[bot]](https://github.com/github-actions[bot])

### Merge
- Merge pull request #84 from datosgobes/feature/convencion-30 ([`148c2de`](https://github.com/datosgobes/DCAT-AP-ES/commit/148c2dec54c192302ba63d619252d070502dac2f)) - [@mjanez](https://github.com/mjanez)
- Merge branch 'develop' into feature/convencion-30 ([`8a97067`](https://github.com/datosgobes/DCAT-AP-ES/commit/8a970679406d0af7949005700a901a29f2300488)) - [@mjanez](https://github.com/mjanez)
- Merge pull request #81 from datosgobes/feature/convencion-25 ([`35410ef`](https://github.com/datosgobes/DCAT-AP-ES/commit/35410ef15f469610e1cb123a13887b75c9b81870)) - [@datos.gob.es](https://github.com/datos.gob.es)

---

## Enero 2026
### Features
- implementar SHACL con Convención 30 para coherencia de taxonomías en temas de datasets y servicios (Convención 30) - `shacl_catalog_shape.ttl`, `shacl_dataservice_shape.ttl`, `shacl_dataset_shape.ttl` ([`f23b81b`](https://github.com/datosgobes/DCAT-AP-ES/commit/f23b81b8407446a53cea270a06af8164a2ee6d0c)) - [@mjanez](https://github.com/mjanez)
- desplazar warning TZ opcional en xsd:dateTime a las formas de entidad - 4 archivos modificados ([`735392a`](https://github.com/datosgobes/DCAT-AP-ES/commit/735392af610ffc003d0e462c7cd2376d2960f57b)) - [@mjanez](https://github.com/mjanez)
- relajar validación estricta de xsd:dateTime sin TZ y recomendar su uso - `shacl_common_shapes.ttl` ([`6d38eef`](https://github.com/datosgobes/DCAT-AP-ES/commit/6d38eef334b749f224b724ae4cd81cf39641e4c0)) - [@mjanez](https://github.com/mjanez)

### Fixes
- crear restricción única WarnDateTimeWithoutTZDConstraint - 4 archivos modificados ([`dbbfac7`](https://github.com/datosgobes/DCAT-AP-ES/commit/dbbfac75d7a4fe9d95ce60e3a47dc58294734ea9)) - [@mjanez](https://github.com/mjanez)

---

## Diciembre 2025
### Features
- añadir validaciones SHACL para convencion 25-26 y 27 (NSIP/ERPD) (Convención 25) - `shacl_dataset_shape.ttl`, `shacl_distribution_shape.ttl` ([`1d0bb69`](https://github.com/datosgobes/DCAT-AP-ES/commit/1d0bb694454c11c843de1bef5b2e4860f5b14263)) - [@mjanez](https://github.com/mjanez)

### Fixes
- agregar restricciones para cumplir la Convención 12 en datasets HVD (Convención 12) - `shacl_dataset_hvd_shape.ttl` ([`dfc78b2`](https://github.com/datosgobes/DCAT-AP-ES/commit/dfc78b249a890e2f6e7151efe3090cf227e1fa28)) - [@mjanez](https://github.com/mjanez)
- corregir errores de formato en las restricciones de la Convención 26 y 27 (Convención 26) - `shacl_distribution_shape.ttl` ([`f2dbc68`](https://github.com/datosgobes/DCAT-AP-ES/commit/f2dbc68a17b6a5a6776a69b6b7bd1e8e8e7df4de)) - [@mjanez](https://github.com/mjanez)
- corregir errores de formato en las restricciones de la Convención 25 y 27 (Convención 25) - `shacl_dataset_shape.ttl` ([`306200e`](https://github.com/datosgobes/DCAT-AP-ES/commit/306200ea82e2add4a5e7bba189e7e7e15a41d142)) - [@mjanez](https://github.com/mjanez)
- actualizar enlaces internos - `shacl_distribution_shape.ttl` ([`0723536`](https://github.com/datosgobes/DCAT-AP-ES/commit/07235360e44e7a2ede3dcb04d2af45002133769e)) - [@mjanez](https://github.com/mjanez)

---

## Octubre 2025
### Other Changes
- Corregidos errores en formas SHACL [SDA-1890] - `shacl_catalog_shape.ttl`, `shacl_common_shapes.ttl`, `shacl_distribution_hvd_shape.ttl` ([`86d08fe`](https://github.com/datosgobes/DCAT-AP-ES/commit/86d08fe8ddb79fd382d291b91b3eb2cb2357e737)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified, normalizar y mejoras de aplicacion del modelo (dcat:CatalogRecord) - `shacl_catalog_shape.ttl` ([`ed2d4d9`](https://github.com/datosgobes/DCAT-AP-ES/commit/ed2d4d9c4e7b2f36200dedacb7f1aa08e992a914)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified, normalizar y mejoras de aplicacion del modelo - `shacl_common_shapes.ttl` ([`ea7d584`](https://github.com/datosgobes/DCAT-AP-ES/commit/ea7d584d426f9a15fe353ac8ea5091e26892e596)) - [@mjanez](https://github.com/mjanez)
- Actualizada fecha de modificacion - `shacl_mdr-vocabularies.shape.ttl` ([`b8f43d6`](https://github.com/datosgobes/DCAT-AP-ES/commit/b8f43d61e6f523faab161df721d69a79034a1733)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified a 2025-10-20 y normalizar referencias foaf:page - `shacl_dataservice_shape.ttl` ([`a462918`](https://github.com/datosgobes/DCAT-AP-ES/commit/a462918b3fa0ee63e13c15a61d3ae57a060ce8ae)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified y normalizar referencias - `shacl_distribution_shape.ttl` ([`a37b08d`](https://github.com/datosgobes/DCAT-AP-ES/commit/a37b08d9e783dd26c4fb8192614498ac4de5109b)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#) y mejorar foaf:page de LicenceTypeRestriction - `shacl_mdr-vocabularies.shape.ttl` ([`720f68e`](https://github.com/datosgobes/DCAT-AP-ES/commit/720f68e0468c6f2457c7cbcb39171ff0f892c8aa)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified , normalizar y añadir propiedades no evaluadas - `shacl_dataset_shape.ttl` ([`66ca79d`](https://github.com/datosgobes/DCAT-AP-ES/commit/66ca79d74c21f208cc2c70191f789946af6f1954)) - [@mjanez](https://github.com/mjanez)
- Usar URI con fragmento (#) en el prefijo dcatapes y actualizar dct:modified a 2025-10-20 - `shacl_imports.ttl` ([`504d419`](https://github.com/datosgobes/DCAT-AP-ES/commit/504d419c5590151fa8eee60f1a8ce296a7beaf08)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#), actualizar dct:modified a 2025-10-20 y normalizar referencias (foaf:page ) en shapes HVD - 4 archivos modificados ([`3ecb65a`](https://github.com/datosgobes/DCAT-AP-ES/commit/3ecb65aa988ec496d6f5070f90754a1f148887f4)) - [@mjanez](https://github.com/mjanez)
- Actualizar prefijo dcatapes a URI con fragmento (#) y actualizar dct:modified a 2025-10-20 - `shacl_mdr_imports.ttl` ([`30458e5`](https://github.com/datosgobes/DCAT-AP-ES/commit/30458e5439b97c49695c8f111f77b69ac8e1e114)) - [@mjanez](https://github.com/mjanez)

---

## Septiembre 2025
### Other Changes
- Mejorada documentación de LicenceDocumentRestriction - `shacl_common_shapes.ttl`, `shacl_mdr-vocabularies.shape.ttl` ([`a6a1fe3`](https://github.com/datosgobes/DCAT-AP-ES/commit/a6a1fe39372261ec66a2d95d390f0cd048168250)) - [@mjanez](https://github.com/mjanez)
- Actualizada la restricción de frecuencia para validar nodos definidos localmente - `shacl_dataset_shape.ttl` ([`9bf3d6c`](https://github.com/datosgobes/DCAT-AP-ES/commit/9bf3d6c31f217fa255c2427c96810af39717c045)) - [@mjanez](https://github.com/mjanez)
- Corregido prefijo geo ausente - `shacl_common_shapes.ttl` ([`5423ad1`](https://github.com/datosgobes/DCAT-AP-ES/commit/5423ad1ffe1abf359b3d97114c7387d734403e1b)) - [@mjanez](https://github.com/mjanez)

---

## Agosto 2025
### Other Changes
- Mejoras en catálogos, datasets, servicios y HVD - 5 archivos modificados ([`a4e9cfb`](https://github.com/datosgobes/DCAT-AP-ES/commit/a4e9cfb4962d016625058b5f4cb3f0ec41a9407b)) - [@mjanez](https://github.com/mjanez)
- Mejorado índice - `README.md` ([`8340050`](https://github.com/datosgobes/DCAT-AP-ES/commit/8340050a3da339fc3d52ce99098af817f26c7de2)) - [@mjanez](https://github.com/mjanez)
- Fix MD - `README.md` ([`7b24455`](https://github.com/datosgobes/DCAT-AP-ES/commit/7b244555ff7d866ce31cff73d25549161cdf313a)) - [@mjanez](https://github.com/mjanez)
- Actualización de la guía de validación SHACL - `README.md` ([`6ae9bc9`](https://github.com/datosgobes/DCAT-AP-ES/commit/6ae9bc9b5b52d57b9e07f637e21e84cf4252f4dd)) - [@mjanez](https://github.com/mjanez)
- Actualización SHACL 18/08 - `shacl_catalog_shape.ttl`, `shacl_dataset_shape.ttl`, `shacl_distribution_shape.ttl` ([`684c237`](https://github.com/datosgobes/DCAT-AP-ES/commit/684c2370c36590dee6acbf917c58a5168d0b727d)) - [@mjanez](https://github.com/mjanez)
- Eliminadas restricciones de tipo Literal en las formas SHACL de Dataset y Distribution innecesarias. - `shacl_dataset_shape.ttl`, `shacl_distribution_shape.ttl` ([`e89c1b0`](https://github.com/datosgobes/DCAT-AP-ES/commit/e89c1b01e01ebfde468c38b4c669542f2a25dfd4)) - [@mjanez](https://github.com/mjanez)
- Añadida restricción para el tipo de conjunto de datos en SHACL - `shacl_dataset_shape.ttl` ([`47db87f`](https://github.com/datosgobes/DCAT-AP-ES/commit/47db87f30e370488c446353a668c1f847a2d1c03)) - [@mjanez](https://github.com/mjanez)
- Actualización SHACL 07-08 - 7 archivos modificados ([`4a1d388`](https://github.com/datosgobes/DCAT-AP-ES/commit/4a1d38822416b739de4a17a72fcc07a737727db5)) - [@mjanez](https://github.com/mjanez)
- Actualizados SHACL 08/2025 - 6 archivos modificados ([`29328f6`](https://github.com/datosgobes/DCAT-AP-ES/commit/29328f61ffbb07b272dbf6409a737a64470e7c80)) - [@mjanez](https://github.com/mjanez)

---

## Junio 2025
### Other Changes
- Corregida errata hasTelephone - `shacl_common_shapes.ttl` ([`ce32fe3`](https://github.com/datosgobes/DCAT-AP-ES/commit/ce32fe33d175b981d298b45f286edada77a8112f)) - [@David Portolés](https://github.com/David Portolés)

---

## Abril 2025
### Other Changes
- Corregido comentario - `shacl_dataset_shape.ttl` ([`63e7cb5`](https://github.com/datosgobes/DCAT-AP-ES/commit/63e7cb5af9f3c4c9f3de6109a67199d8302f6b39)) - [@mjanez](https://github.com/mjanez)
- Refactorización de los archivos de validación SHACL - 11 archivos modificados ([`dd65219`](https://github.com/datosgobes/DCAT-AP-ES/commit/dd652192c78530dd8b9cfb5044da88bcb2f0a7c1)) - [@mjanez](https://github.com/mjanez)
- Eliminada restricción de idioma único en tags - `shacl_dataservice_shape.ttl`, `shacl_dataset_shape.ttl` ([`7baa420`](https://github.com/datosgobes/DCAT-AP-ES/commit/7baa420ce7eb7f82d39f9780ef2d3bc83520cb81)) - [@mjanez](https://github.com/mjanez)
- Actualizado README validacion - `README.md` ([`a4721b7`](https://github.com/datosgobes/DCAT-AP-ES/commit/a4721b7208119c1584fe19f10808f1c6e2540b9e)) - [@mjanez](https://github.com/mjanez)
- Actualiza las URLs de descarga y referencia en el archivo SHACL - `shacl_dataset_hvd_shape.ttl` ([`5eb7087`](https://github.com/datosgobes/DCAT-AP-ES/commit/5eb70878bb481a52a55f2e6113387e0215235335)) - [@mjanez](https://github.com/mjanez)
- Añadidos SHACL para DCAT-AP-ES - 12 archivos modificados ([`5cd53f8`](https://github.com/datosgobes/DCAT-AP-ES/commit/5cd53f8dddae845a25cfc4a22286ce94b626b655)) - [@mjanez](https://github.com/mjanez)
- Actualiza la documentación de validación SHACL en inglés y español, mejorando la claridad y añadiendo ejemplos de uso. - `README.md` ([`ce93c31`](https://github.com/datosgobes/DCAT-AP-ES/commit/ce93c31cbf0807b2b2dbf1a24b860c82d73719e9)) - [@mjanez](https://github.com/mjanez)

---


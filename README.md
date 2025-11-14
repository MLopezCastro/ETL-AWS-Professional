# 🚀 **Serverless ETL Pipeline in AWS – From CSV to Athena Query (2025)**

## 📌 **Overview**

Este proyecto implementa un pipeline **ETL 100% serverless** en AWS usando **S3, Lambda, Athena y Step Functions**, automatizando desde la carga de un CSV hasta la obtención de resultados de consulta en Athena, todo sin servidores y en la nube.

💡 **Caso práctico:**
Una empresa de e-commerce quiere automatizar el procesamiento de sus pedidos:

1. Un archivo `orders.csv` se sube a S3.
2. Un Lambda convierte el CSV a **Parquet con compresión Snappy** para optimizar almacenamiento y consultas.
3. Athena consulta datos agregados de ventas por estado.
4. El resultado se guarda automáticamente en S3 para consumo en BI.

---

## 📂 **Estructura del proyecto (local)**

```bash
aws-etl-pipeline/
├── data/
│   ├── raw/
│   │   ├── orders.csv                 # ✅ Input local
│   │   └── customers.csv
│   └── output/
│       ├── orders_clean.csv
│       ├── orders_clean.parquet
│       └── orders_clean.snappy.parquet
├── lambda_query/
│   ├── handler.py                     # ✅ Lambda Athena
│   └── lambda-package/                # Dependencias ZIP
├── scripts/
│   ├── aws_uploader.py
│   ├── export.py
│   ├── helpers.py
│   ├── step_executor.py
│   ├── transform.py
│   └── validate.py
├── logs/
│   └── etl.log
├── UploadLambda.zip                    # Lambda CSV → Parquet
├── athenaQueryLambda.zip               # Lambda Athena
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔄 **Flujo del Pipeline**

<img width="647" height="648" alt="image" src="https://github.com/user-attachments/assets/8b1677ac-06f5-45ff-a59e-08d36f58096e" />

---

## 🛠 **Tecnologías**

* **AWS S3** – Almacenamiento de datos
* **AWS Lambda** – Procesamiento sin servidor
* **AWS Athena** – Consultas SQL sobre datos en S3
* **AWS Step Functions** – Orquestación del pipeline
* **Python 3.10** – Scripts y Lambdas
* **Parquet + Snappy** – Formato y compresión optimizados

---

## 📍 **Implementación paso a paso**

### 1️⃣ Subir CSV inicial a S3

```bash
aws s3 mb s3://marcelo-orders-bucket
aws s3 cp data/raw/orders.csv s3://marcelo-orders-bucket/data/orders.csv
```

<img width="532" height="688" alt="image" src="https://github.com/user-attachments/assets/219b3376-192d-40ec-9cad-3b152952f670" />

---

### 2️⃣ Lambda 1 – `uploadLambda` (CSV → Parquet)

* Creada manualmente en la consola de AWS Lambda
* Convierte el CSV a Parquet con compresión Snappy
* Guarda el archivo optimizado en S3

<img width="830" height="792" alt="image" src="https://github.com/user-attachments/assets/730efd49-7dbc-403b-92a0-759560ac5fa6" />

<img width="986" height="332" alt="image" src="https://github.com/user-attachments/assets/d459137d-eb77-4054-a593-ead7608ff7df" />

---

### 3️⃣ Crear tabla externa en Athena

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS default.orders_clean (
  order_id BIGINT,
  order_date DATE,
  customer_id BIGINT,
  product_id BIGINT,
  product_name STRING,
  quantity BIGINT,
  unit_price DOUBLE,
  currency STRING,
  status STRING,
  total_amount DOUBLE
)
STORED AS PARQUET
LOCATION 's3://marcelo-orders-bucket/data/'
TBLPROPERTIES ('parquet.compress'='SNAPPY');
```

<img width="942" height="446" alt="image" src="https://github.com/user-attachments/assets/cb11d275-c6ba-4497-b5ac-20920fd19c5d" />

<img width="839" height="509" alt="image" src="https://github.com/user-attachments/assets/27ed128b-0eb5-4fe1-9ced-99c595baef94" />

---

### 4️⃣ Lambda 2 – `athenaQueryLambda` (Query → S3)

* Subida como ZIP (`athenaQueryLambda.zip`)
* Ejecuta query en Athena:

```sql
SELECT status, SUM(total_amount) AS total_sales
FROM default.orders_clean
GROUP BY status;
```

* Guarda resultados en `s3://marcelo-orders-bucket/athena-results/`

<img width="793" height="818" alt="image" src="https://github.com/user-attachments/assets/1c019ee0-1e29-4dce-b782-e1d517654c86" />

---

### 5️⃣ Orquestación con Step Functions

* Task 1: Ejecuta `uploadLambda`
* Task 2: Ejecuta `athenaQueryLambda`

* Diagrama visual de la Step Function en AWS

<img width="841" height="571" alt="image" src="https://github.com/user-attachments/assets/d32d3c46-9e0e-4931-a27e-3912b47e629e" />

* Ejecución exitosa con input:

<img width="1125" height="809" alt="image" src="https://github.com/user-attachments/assets/f04f96ba-f252-446d-951b-040c976c32fd" />


```json
{
  "bucket": "marcelo-orders-bucket",
  "key": "data/orders.csv"
}
```

---

### 6️⃣ Resultados finales

* CSV convertido y optimizado en Parquet
* Query ejecutada automáticamente
* Resultados listos en S3 para ser consumidos por Power BI, Tableau u otra herramienta

<img width="1607" height="683" alt="image" src="https://github.com/user-attachments/assets/566f2a7c-f3d7-44b2-bc73-227b97d3db6b" />

<img width="190" height="144" alt="csvdelambda" src="https://github.com/user-attachments/assets/f2e2ef7c-68ea-459e-94cd-f5e4e9d0c977" />

---

## 📈 **Valor práctico**

* **Escalabilidad:** procesamiento de grandes volúmenes de datos sin servidores
* **Costo optimizado:** pago por uso, almacenamiento eficiente con Parquet/Snappy
* **Automatización:** elimina procesos manuales de conversión y consulta
* **Integración directa con BI:** datos listos para análisis

---

## 📷 **Lista de imágenes a preparar**

1. **Diagrama general** (el `graph TD` que ya tienes)
2. **VSCode – estructura del proyecto**
3. **S3 con el CSV original**
4. **Lambda `uploadLambda` en consola**
5. **S3 con el Parquet generado**
6. **Athena – tabla creada**
7. **Lambda `athenaQueryLambda` en consola**
8. **Step Function – diagrama visual**
9. **Step Function – ejecución exitosa**
10. **S3 con carpeta `athena-results/` y archivo de salida**

---



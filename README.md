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

📷 **Imagen a incluir:** S3 mostrando `orders.csv`

---

### 2️⃣ Lambda 1 – `uploadLambda` (CSV → Parquet)

* Creada manualmente en la consola de AWS Lambda
* Convierte el CSV a Parquet con compresión Snappy
* Guarda el archivo optimizado en S3

📷 **Imagen a incluir:**

* Pantalla de AWS Lambda con `uploadLambda` y su código
* S3 mostrando el `.parquet` generado

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

📷 **Imagen a incluir:** Athena con la tabla creada

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

📷 **Imagen a incluir:** AWS Lambda con `athenaQueryLambda`

---

### 5️⃣ Orquestación con Step Functions

* Task 1: Ejecuta `uploadLambda`
* Task 2: Ejecuta `athenaQueryLambda`

📷 **Imagen a incluir:**

* Diagrama visual de la Step Function en AWS
* Ejecución exitosa con input:

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

📷 **Imagen a incluir:** S3 mostrando carpeta `athena-results/`

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

Si querés, ahora te puedo dar también la **versión reducida en inglés** para LinkedIn y portfolio, usando este README como base, así cierras todo hoy.
¿Querés que lo arme ahora mismo?




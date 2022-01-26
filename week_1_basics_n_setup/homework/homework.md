## Week 1 Homework

In this homework we'll prepare the environment 
and practice with terraform and SQL

## Question 1. Google Cloud SDK

Install Google Cloud SDK. What's the version you have? 

To get the version, run `gcloud --version`
### Answers
```
Google Cloud SDK 370.0.0
beta 2022.01.21
bq 2.0.73
core 2022.01.21
gsutil 5.6
```

## Google Cloud account 

Create an account in Google Cloud and create a project.


## Question 2. Terraform 

Now install terraform and go to the terraform directory (`week_1_basics_n_setup/1_terraform_gcp/terraform`)

After that, run

* `terraform init`
* `terraform plan`
* `terraform apply` 

Apply the plan and copy the output (after running `apply`) to the form.

It should be the entire output - from the moment you typed `terraform init` to the very end.
### Answers
- `terraform init`
```
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/google from the dependency lock file
- Using previously-installed hashicorp/google v4.8.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

```
- `terraform plan`
```
var.project
  Your GCP Project ID

  Enter a value: [******************]


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "[******************]"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_[******************]"
      + project                     = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_storage_class = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.

```
- `terraform apply`
```
var.project
  Your GCP Project ID

  Enter a value: [******************]


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "[******************]"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_[******************]"
      + project                     = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_storage_class = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 2s [id=projects/[******************]/datasets/trips_data_all]
google_storage_bucket.data-lake-bucket: Creation complete after 3s [id=dtc_data_lake_[******************]]

``` 
## Prepare Postgres 

Run Postgres and load data as shown in the videos

We'll use the yellow taxi trips from January 2021:

```bash
wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv
```

You will also need the dataset with zones:

```bash 
wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
```

Download this data and put it to Postgres

## Question 3. Count records 

How many taxi trips were there on January 15?
### Answers
```
SELECT
	COUNT(1)
FROM
	yellow_taxi_data ytd
WHERE CAST(ytd.tpep_pickup_datetime AS DATE) = '2021-01-15';

Results
count|
-----+
53024|
```

Consider only trips that started on January 15.
### Answers
```
SELECT
	COUNT(1)
FROM
	yellow_taxi_data ytd
WHERE CAST(ytd.tpep_pickup_datetime AS DATE) >= '2021-01-15';

Results
count |
------+
771424|
```


## Question 4. Largest tip for each day

Find the largest tip for each day. 
On which day it was the largest tip in January?

Use the pick up time for your calculations.

(note: it's not a typo, it's "tip", not "trip")

```
SELECT
	CAST(ytd.tpep_pickup_datetime AS DATE) AS DAY,
	MAX(ytd.tip_amount) AS largest_tip
FROM
	yellow_taxi_data ytd
WHERE
	CAST(ytd.tpep_pickup_datetime AS DATE) >= '2021-01-01' AND
	CAST(ytd.tpep_pickup_datetime AS DATE) <= '2021-01-31'
GROUP BY DAY
ORDER BY largest_tip DESC
----------+-----------+
day       |largest_tip|
----------+-----------+
2021-01-20|    1140.44|
2021-01-04|     696.48|
2021-01-03|      369.4|
2021-01-26|      250.0|
2021-01-09|      230.0|
2021-01-19|      200.8|
2021-01-30|     199.12|
2021-01-12|     192.61|
2021-01-21|      166.0|
2021-01-01|      158.0|
2021-01-05|      151.0|
2021-01-11|      145.0|
2021-01-24|      122.0|
2021-01-02|     109.15|
2021-01-31|      108.5|
2021-01-25|     100.16|
2021-01-16|      100.0|
2021-01-13|      100.0|
2021-01-23|      100.0|
2021-01-08|      100.0|
2021-01-27|      100.0|
2021-01-06|      100.0|
2021-01-15|       99.0|
2021-01-07|       95.0|
2021-01-14|       95.0|
2021-01-22|      92.55|
2021-01-10|       91.0|
2021-01-18|       90.0|
2021-01-28|      77.14|
2021-01-29|       75.0|
2021-01-17|       65.0|
```


## Question 5. Most popular destination

What was the most popular destination for passengers picked up 
in central park on January 14?

Use the pick up time for your calculations.

Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown" 

### Answers 
- Zone name is Upper East Side South
```
  	
WITH Zones AS (
SELECT
	"index",
	z."LocationID",
	z."Borough" ,
	COALESCE(z."Zone" , 'Unknown') AS "Zone",
	z.service_zone
FROM
	zones z 
	)
SELECT
	do_zone."Zone",
	count(1) AS count_do
FROM
	yellow_taxi_data ytd
LEFT JOIN Zones AS pu_zone 
ON
	ytd."PULocationID" = pu_zone."LocationID"
LEFT JOIN Zones AS do_zone 
ON
	ytd."DOLocationID" = do_zone."LocationID"
WHERE
	pu_zone."Zone" = 'Central Park'
	AND CAST(ytd.tpep_pickup_datetime AS DATE) = '2021-01-14'
GROUP BY do_zone."Zone" 
ORDER BY count_do DESC
------------------------------+--------+
Zone                          |count_do|
------------------------------+--------+
Upper East Side South         |      97|
Upper East Side North         |      94|
Lincoln Square East           |      83|
Upper West Side North         |      68|
Upper West Side South         |      60|
Central Park                  |      59|
Midtown Center                |      56|
Yorkville West                |      40|
Lenox Hill West               |      39|
Lincoln Square West           |      36|
Midtown North                 |      30|
Yorkville East                |      25|
Manhattan Valley              |      24|
Midtown East                  |      23|
East Harlem South             |      22|
Lenox Hill East               |      21|
Murray Hill                   |      20|
Midtown South                 |      19|
Clinton East                  |      19|
Garment District              |      18|
Union Sq                      |      15|
West Chelsea/Hudson Yards     |      13|
Central Harlem                |      13|
UN/Turtle Bay South           |      12|
Sutton Place/Turtle Bay North |      12|
Little Italy/NoLiTa           |      11|
Morningside Heights           |      11|
Clinton West                  |      10|
Greenwich Village North       |       9|
Times Sq/Theatre District     |       9|
West Village                  |       8|
East Harlem North             |       8|
Washington Heights South      |       7|
East Chelsea                  |       7|
Gramercy                      |       6|
Hamilton Heights              |       5|
Central Harlem North          |       5|
Meatpacking/West Village West |       5|
Flatiron                      |       4|
Bloomingdale                  |       4|
East Village                  |       4|
Steinway                      |       3|
TriBeCa/Civic Center          |       3|
NV                            |       3|
Washington Heights North      |       3|
Manhattanville                |       2|
Financial District North      |       2|
Greenwich Village South       |       2|
Hudson Sq                     |       2|
Kips Bay                      |       2|
Long Island City/Hunters Point|       2|
Lower East Side               |       2|
Battery Park City             |       2|
Penn Station/Madison Sq West  |       2|
SoHo                          |       2|
Stuy Town/Peter Cooper Village|       2|
Sunset Park West              |       2|
Boerum Hill                   |       1|
Sunnyside                     |       1|
Bay Ridge                     |       1|
Pelham Bay                    |       1|
Park Slope                    |       1|
Old Astoria                   |       1|
Ocean Hill                    |       1|
Morrisania/Melrose            |       1|
Jackson Heights               |       1|
Inwood                        |       1|
Flatlands                     |       1|
Flatbush/Ditmas Park          |       1|
East Williamsburg             |       1|
East Flatbush/Farragut        |       1|
Eastchester                   |       1|
Crown Heights South           |       1|
Williamsbridge/Olinville      |       1|
Windsor Terrace               |       1|
Spuyten Duyvil/Kingsbridge    |       1|
Seaport                       |       1|
```


## Question 6. Most expensive locations

What's the pickup-dropoff pair with the largest 
average price for a ride (calculated based on `total_amount`)?

Enter two zone names separated by a slash

For example:

"Jamaica Bay / Clinton East"

If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East". 

### Answers
```
WITH Zones AS (
SELECT
	"index",
	z."LocationID",
	z."Borough" ,
	COALESCE(z."Zone" , 'Unknown') AS "Zone",
	z.service_zone
FROM
	zones z 
	)
SELECT
	pu_zone."Zone" AS pu_zone,
	do_zone."Zone" AS do_zone,
	AVG(ytd.total_amount) AS average_total_amount 
FROM
	yellow_taxi_data ytd
LEFT JOIN Zones AS pu_zone 
ON
	ytd."PULocationID" = pu_zone."LocationID"
LEFT JOIN Zones AS do_zone 
ON
	ytd."DOLocationID" = do_zone."LocationID"
GROUP BY pu_zone."Zone", do_zone."Zone" 
ORDER BY average_total_amount DESC

** show some result from output
-----------------------------------+-----------------------------------+--------------------+
pu_zone                            |do_zone                            |average_total_amount|
-----------------------------------+-----------------------------------+--------------------+
Alphabet City                      |Unknown                            |              2292.4|
Union Sq                           |Canarsie                           |  262.85200000000003|
Ocean Hill                         |Unknown                            |              234.51|
Long Island City/Hunters Point     |Clinton East                       |              207.61|
Boerum Hill                        |Woodside                           |               200.3|
Baisley Park                       |Unknown                            |            181.4425|
Bushwick South                     |Long Island City/Hunters Point     |              156.96|
Willets Point                      |Unknown                            |              154.42|
Co-Op City                         |Dyker Heights                      |              151.37|
Rossville/Woodrow                  |Pelham Bay Park                    |               151.0|
Charleston/Tottenville             |Woodlawn/Wakefield                 |              149.99|
Borough Park                       |NV                                 |              149.53|
Eastchester                        |Charleston/Tottenville             |  148.43333333333334|
```

## Submitting the solutions

* Form for submitting: https://forms.gle/yGQrkgRdVbiFs8Vd7
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 26 January (Wednesday), 22:00 CET


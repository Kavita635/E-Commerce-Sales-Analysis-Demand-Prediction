# Data Dictionary

## Project
E-Commerce Sales Analysis & Demand Prediction

Dataset: DataCoSupplyChainDataset.csv

Total Rows: 180,519

Total Columns: 53

## Customer Information
| Column            |        Description         | Keep?  |
|-------------------|----------------------------|--------|
| Customer Id       | Unique customer identifier | ✅ Yes |
| Customer Fname    | Customer first name        | ❌ No  |
| Customer Lname    | Customer last name         | ❌ No  |
| Customer Email    | Customer email             | ❌ No  |
| Customer Password | Customer password          | ❌ No  |
| Customer Segment  | Customer type/segment      | ✅ Yes |
| Customer City     | Customer city              | ✅ Yes |
| Customer State    | Customer state             | ✅ Yes |
| Customer Country  | Customer country           | ✅ Yes |
| Customer Street   | Customer address           | ❌ No  |
| Customer Zipcode  | Postal code                | ❌ No  |

## Product Information
| Column              | Description           | Keep?  |
|---------------------|-----------------------|--------|
| Product Card Id     | Product ID            | ✅ Yes |
| Product Category Id | Category ID           | ✅ Yes |
| Category Name       | Product category      | ✅ Yes |
| Product Name        | Product name          | ✅ Yes |
| Product Price       | Product selling price | ✅ Yes |
| Product Status      | Product availability  | ✅ Yes |
| Product Image       | Image URL             | ❌ No  |
| Product Description | Product description   | ❌ No (Entire column missing) |

## Order Information
| Column                   |        Description     | Keep?  |
|--------------------------|------------------------|--------|
| Order Id                 | Order identifier       | ✅ Yes |
| Order Customer Id        | Customer placing order | ✅ Yes |
| Order Item Id            | Order item identifier  | ❌ No  |
| Order Item Quantity      | Quantity purchased     | ✅ Yes |
| Order Item Product Price | Product price in order | ✅ Yes |
| Order Item Discount      | Discount amount        | ✅ Yes |
| Order Item Discount Rate | Discount percentage    | ✅ Yes |
| Sales                    | Total sales            | ✅ Yes |
| Order Item Total         | Final order value      | ✅ Yes |
| Benefit per Order        | Profit earned          | ✅ Yes |
| Order Profit Per Order   | Profit per order       | ✅ Yes |

## Shipping Information
| Column                        |     Description         | Keep? |
|-------------------------------|-------------------------|--------|
| Shipping Mode                 | Shipping method         | ✅ Yes |
| Delivery Status               | Delivery status         | ✅ Yes |
| Days for shipment (scheduled) | Planned shipping days   | ✅ Yes |
| Days for shipping (real)      | Actual shipping days    | ✅ Yes |
| Late_delivery_risk            | Late delivery indicator | ✅ Yes |
| shipping date (DateOrders)    | Shipping date           | ✅ Yes |

## Location Information
| Column        | Description            | Keep?  |
|---------------|------------------------|--------|
| Order City    | Order city             | ✅ Yes |
| Order State   | Order state            | ✅ Yes |
| Order Country | Order country          | ✅ Yes |
| Order Region  | Region                 | ✅ Yes |
| Order Zipcode | Postal code            | ❌ No (Too many missing values) |
| Latitude      | Latitude               | ❌ No  |
| Longitude     | Longitude              | ❌ No  |
| Market        | Market/Business region | ✅ Yes |

## Date Information
| Column                     | Description   | Keep?  |
|----------------------------|---------------|--------|
| order date (DateOrders)    | Order date    | ✅ Yes |
| shipping date (DateOrders) | Shipping date | ✅ Yes |

## Columns to Remove During Cleaning
- Customer Email
- Customer Password
- Customer Street
- Customer Zipcode
- Product Image
- Product Description
- Order Zipcode
- Latitude
- Longitude

## Initial Observations
- The dataset contains 180,519 records and 53 columns.
- There are no duplicate records.
- Most columns are complete with very few missing values.
- Product Description is completely empty and will be removed.
- Order Zipcode has a large number of missing values and is likely to be removed.
- The dataset includes customer, product, order, shipping, and geographical information.
- The dataset is suitable for sales analysis and demand prediction.
- The tentative target variable is Order Item Quantity.

## Missing Value Analysis
### Product Description
- Missing: 100%
- Decision: Removed
- Reason: Column contains no information.

### Customer Lname
- Missing: 8 values
- Decision: Removed
- Reason: Personal information; not useful for analysis.

### Customer Zipcode
- Missing: 3 values
- Decision: Keep for now
- Reason: Missing percentage is negligible.

### Order Zipcode
- Missing: 86%
- Decision: Pending
- Reason: Large amount of missing data; evaluate its usefulness before removal.
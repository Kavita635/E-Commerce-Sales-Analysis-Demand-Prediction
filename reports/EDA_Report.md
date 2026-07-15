1. Sales Trend Over Time
Business Objective-
  Analyze how sales changed over time to identify trends and demand fluctuations.
Observation-
  Sales remained relatively stable from 2015 to 2017.
  A slight increase is visible during mid-2017.
  The decline in the last few months is due to incomplete data rather than reduced sales.
Business Insight-
  Sales demand was consistent throughout most of the dataset period, indicating stable business performance. The lower sales values at the end of the timeline are caused by incomplete records.
Recommendation-
  Use complete monthly data for future forecasting.
  Continue monitoring monthly sales trends to identify seasonal demand.

2. Top 10 Products by Sales Revenue
Business Objective-
  Identify the products generating the highest revenue.
Observation
  Field & Stream Sportsman 16 Gun Fire Safe generated the highest sales revenue.
  The top-selling products contribute a significant portion of the company's revenue.
Business Insight-
  High-revenue products should receive priority in inventory planning because stock shortages for these products could directly impact overall revenue.
Recommendation-
  Maintain sufficient inventory for high-revenue products.
  Use these products in promotional campaigns.
  Monitor their demand regularly.

3. Top 10 Products by Quantity Sold
Business Objective-
  Identify the products that customers purchase most frequently to understand product demand.
Observation-
  Perfect Fitness Perfect Rip Deck has the highest quantity sold (73,698 units).
  Nike Men's Dri-FIT Victory Golf Polo is the second most purchased product.
  O'Brien Men's Neoprene Life Vest also shows strong customer demand.
  Some products generate high sales because of high purchase quantity rather than a high selling price.
Business Insight
  Products with the highest purchase quantities represent strong customer demand and should always remain available in inventory. Frequent stock-outs of these products may result in lost sales and dissatisfied customers.
Recommendation-
  Maintain higher inventory levels for fast-moving products.
  Use demand forecasting to avoid stock shortages.
  Analyze why these products are popular and apply similar strategies to other products.

4. Region-wise Sales Performance
Business Objective-
  Identify the regions generating the highest sales revenue to understand the company's strongest markets.
Observation-
  Western Europe generated the highest sales revenue (approximately 5.89 million).
  Central America is the second highest-performing region (approximately 5.65 million).
  South America ranks third with around 2.97 million in sales.
  Central Asia generated the lowest sales revenue among all regions.
Business Insight-
  The company has a strong customer base and market presence in Western Europe and Central America. These regions contribute a significant portion of the overall revenue, while regions like Central Asia, Canada, and parts of Africa show comparatively lower sales and may require additional business attention.
Recommendation-
  Continue investing in high-performing regions to maintain revenue growth.
  Improve marketing campaigns and promotional offers in low-performing regions.
  Analyze customer preferences and local market conditions in regions with low sales to identify growth opportunities.

  5. Category-wise Sales Analysis
Business Objective-
  Identify which product categories contribute the highest sales revenue.
Observation-
  Fishing is the highest revenue-generating category (approximately 6.9 million).
  Cleats and Camping & Hiking are the second and third highest-selling categories.
  Categories such as Books, Baby, Toys, and CDs contribute very little to the total sales.
  Sales are highly concentrated in a few major categories.
Business Insight-
  A small number of product categories generate most of the company's revenue. This indicates that customer demand is focused on outdoor sports and fitness-related products, while many other categories have comparatively low demand.
Recommendation-
  Maintain sufficient inventory for high-performing categories like Fishing and Cleats.
  Increase marketing efforts for medium-performing categories to improve sales.
  Evaluate whether low-performing categories should be promoted, redesigned, or discontinued based on profitability.

6. Shipping Mode Analysis
Business Objective-
  Analyze customer preferences for different shipping methods and identify which shipping mode contributes the most to sales.
Observation-
  Standard Class generated the highest sales revenue (approximately 22 million).
  Second Class is the second most preferred shipping method.
  First Class contributes a moderate amount of sales.
  Same Day shipping has the lowest sales among all shipping modes.
Business Insight-
  Most customers prefer Standard Class shipping, suggesting they prioritize lower shipping costs over faster delivery. Premium shipping options are used by fewer customers, indicating that delivery speed is not the primary factor influencing most purchasing decisions.
Recommendation-
  Continue optimizing Standard Class logistics since it handles the majority of orders.
  Promote First Class and Same Day shipping through discounts or special offers for urgent deliveries.
  Analyze whether premium shipping charges are discouraging customers from choosing faster delivery options

6. Delivery Time Distribution
Business Objective-
  Analyze the distribution of delivery time to understand shipping performance and identify delivery patterns.
Observation-
  The average delivery time is approximately 3.5 days.
  Most orders are delivered within 2–5 days.
  Very few orders are delivered on the same day (0–1 day).
  The maximum delivery time recorded is 6 days.
Business Insight-
  The company maintains a consistent delivery performance, with the majority of orders being completed within a reasonable time frame. The limited number of same-day deliveries suggests that faster delivery services are used selectively.
Recommendation-
  Continue maintaining delivery within 2–5 days.
  Increase availability of faster shipping options for premium customers.
  Monitor orders approaching the 6-day delivery limit to improve customer satisfaction.

7. Correlation Heatmap
Business Objective-
  Analyze relationships among numerical variables to identify important features that influence sales and demand prediction.
Observation-
  Sales shows a strong positive correlation with Sales per Customer and Order Item Total.
  Product Price has a moderate positive relationship with Sales.
  Most remaining features have weak or negligible correlations.
  No severe multicollinearity is observed among the majority of variables.
Business Insight-
  Revenue is primarily driven by customer spending and total order value rather than individual identifiers or geographical variables. This indicates that pricing and purchasing behavior have a greater impact on sales than customer or location information.
Recommendation-
  Prioritize highly correlated variables such as Sales per Customer, Order Item Total, and Product Price during feature selection.
  Remove low-impact or identifier columns before machine learning to reduce model complexity.
  Use the correlation matrix to avoid selecting redundant features during model training.
-- Q7. Write a query to display carton id, (len*width*height) as carton_vol and identify the
-- optimum carton (carton with the least volume whose volume is greater than the total
-- volume of all items (len * width * height * product_quantity)) for a given order whose order
-- id is 10006, Assume all items of an order are packed into one single carton (box). (

SELECT CARTON_ID, (LEN*WIDTH*HEIGHT) AS CARTON_VOL
FROM CARTON WHERE (LEN*WIDTH*HEIGHT) > (SELECT sum(p.len*p.width*p.height*oi.product_quantity) as Volume 
from product p 
INNER JOIN order_items oi ON p.product_id = oi.product_id
WHERE order_id = 10006)
ORDER BY CARTON_VOL 
LIMIT 1;

-- Q8.  Write a query to display details (customer id,customer fullname,order id,product
-- quantity) of customers who bought more than ten (i.e. total order qty) products per shipped
-- order.

SELECT oc.CUSTOMER_ID, CONCAT(oc.CUSTOMER_FNAME," ",oc.CUSTOMER_LNAME) AS FULL_NAME, oh.ORDER_ID, sum(oi.PRODUCT_QUANTITY) as TOTAL_ORDER_QUANTITY
FROM ONLINE_CUSTOMER oc
INNER JOIN  ORDER_HEADER oh ON oc.CUSTOMER_ID = oh.CUSTOMER_ID
INNER JOIN ORDER_ITEMS oi ON oh.ORDER_ID = oi.ORDER_ID
WHERE oh.ORDER_STATUS = "SHIPPED"
GROUP BY oh.ORDER_ID
HAVING TOTAL_ORDER_QUANTITY > 10;

-- Q9. Write a query to display the order_id, customer id and cutomer full name of customers
-- along with (product_quantity) as total quantity of products shipped for order ids > 10060. 

SELECT oh.ORDER_ID, oc.CUSTOMER_ID, CONCAT(oc.CUSTOMER_FNAME," ",oc.CUSTOMER_LNAME) AS FULL_NAME, sum(oi.PRODUCT_QUANTITY) as TOTAL_QUANTITY
FROM ONLINE_CUSTOMER oc
INNER JOIN  ORDER_HEADER oh ON oc.CUSTOMER_ID = oh.CUSTOMER_ID
INNER JOIN ORDER_ITEMS oi ON oh.ORDER_ID = oi.ORDER_ID
WHERE oh.ORDER_STATUS = "SHIPPED" AND oh.ORDER_ID > 10060
GROUP BY oh.ORDER_ID;

-- Q10. Write a query to display product class description ,total quantity
-- (sum(product_quantity),Total value (product_quantity * product price) and show which class
-- of products have been shipped highest(Quantity) to countries outside India other than USA?
-- Also show the total value of those items.

select pc.product_class_desc, sum(oi.product_quantity) as Total_Quantity, SUM(oi.product_quantity * p.product_price) as Total_Value -- max(Product_Class_Desc) 
from ADDRESS ad
INNER JOIN ONLINE_CUSTOMER oc ON ad.ADDRESS_ID = oc.ADDRESS_ID
INNER JOIN  ORDER_HEADER oh ON oh.CUSTOMER_ID = oc.CUSTOMER_ID
INNER JOIN  ORDER_ITEMS oi ON oh.ORDER_ID = oi.ORDER_ID
INNER JOIN  PRODUCT p ON oi.PRODUCT_ID = p.PRODUCT_ID
INNER JOIN PRODUCT_CLASS pc ON p.PRODUCT_CLASS_CODE = pc.PRODUCT_CLASS_CODE
where ad.COUNTRY NOT IN ("INDIA","USA")
group by pc.product_class_desc
order by total_quantity desc LIMIT 1;
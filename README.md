## CREATOR LEARNING PLATFORM

# Tech Stack
. Django
. Django REST Framework
. PostgreSQL
. Redis
. Celery
. JWT Authentication


## Use of subscription billing logic:

. The subscription billing logic is added in the subscriptions apps file named service file of this project and then this service file method made with the use of transaction.atomic decorator is used in the SubscriptionViewset.

 - Now it works in a manner like when a subscriber sends a POST method request with the plan_id and the pay_method_id, then in this case first the service will get/fetch the plan and alongside it the payment method owned by the subscribers
 
 . Then after this it will create a subscription for the user by calculating the start and the expiry dates and also this is based on the plan type like whether its a monthly or a yearly plan.
 
 - Further then after all of this a invoice and the invoice item are going to be created automatically, and also a payment is going to be recorded as a success.
 
  - And in the end the status of invoice is going to be updated to paid, then the viewset will call this service method, also the logic of subscription is going to be serialized and then it will simply eturn a response. So the use of this full subscription billing logic makes sure that the subscribers can only use their own payment methods and also all the data which is created is safely handled inside a single transaction.


## Use of Lesson Progress checking logic:
. The addition of lesson progress checking logic is about allowing the subscribers to be able to mark the essons as completed. 
. Now according to this logic When a POST method request is sended with the id of lesson , then on this the service function will update and create the record for the LessonProgress related to that user and it will also mark the lesson as completed.

 - Further it will also cal. the total num of lessons in the course alongside the num of comp lessons by that user.
- Then after this the service function is called in the viewset and on doing this it returns the sttus of completion as well as the progress % of the updated course.
import json
import boto3
import uuid

# Connect to DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PizzaOrders')  # Your DynamoDB table name

def lambda_handler(event, context):
    intent_name = event['sessionState']['intent']['name']
    
    if intent_name == 'PizzaOrder':
        slots = event['sessionState']['intent']['slots']
        
        # Extract values from slots
        order_id = str(uuid.uuid4())
        pizza_size = slots['PizzaSize']['value']['interpretedValue']
        crust = slots['CrustType']['value']['interpretedValue']
        toppings = slots['Toppings']['value']['interpretedValue']
        customer_name = slots['CustomerName']['value']['interpretedValue']
        address = slots['DeliveryAddress']['value']['interpretedValue']
        phone = slots['ContactNumber']['value']['interpretedValue']
        delivery_time = slots['DeliveryTime']['value']['interpretedValue']
        
        # Store order in DynamoDB
        table.put_item(
            Item={
                'orderId': order_id,
                'customerName': customer_name,
                'size': pizza_size,
                'crust': crust,
                'toppings': toppings,
                'address': address,
                'phone': phone,
                'deliveryTime': delivery_time
            }
        )
        
        # Reply to user
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": "PizzaOrder",
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Thank you {customer_name}! Your {pizza_size} pizza with {crust} crust and {toppings} will be delivered at {delivery_time} to {address}. We'll contact you at {phone}. Your Order ID is {order_id}."
                }
            ]
        }
    
    elif intent_name == 'CancelOrder':
        slots = event['sessionState']['intent']['slots']
        order_id = slots['OrderID']['value']['interpretedValue']
        
        try:
            # Delete from DynamoDB
            table.delete_item(
                Key={'orderId': order_id}
            )
            
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "Close"
                    },
                    "intent": {
                        "name": "CancelOrder",
                        "state": "Fulfilled"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f"Your order with ID {order_id} has been successfully cancelled."
                    }
                ]
            }
        except Exception as e:
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "Close"
                    },
                    "intent": {
                        "name": "CancelOrder",
                        "state": "Failed"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f"Sorry, I couldn’t cancel your order. Error: {str(e)}"
                    }
                ]
            }

    # Fallback if intent is not matched
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name,
                "state": "Failed"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Sorry, I didn't understand your request. Please try again."
            }
        ]
    }

from datetime import datetime

from main.models import Customer, Order
from main.serializers.serializers_customer import CustomerSerializer


def get_customer_info(customer: Customer) -> dict:
    return CustomerSerializer(customer).data


def create_customer(email: str, first_name: str, last_name: str, phone: str,
                    middle_name: str, username: str, birthday: str,
                    password: str) -> Customer:
    customer = Customer(email=email, first_name=first_name, last_name=last_name,
                        phone=phone, middle_name=middle_name, username=username)
    customer.set_password(password)

    if birthday:
        customer.birthday = datetime.strptime(birthday, '%d.%m.%Y')

    customer.save()
    set_customer_orders(customer)
    return customer


def set_customer_orders(customer: Customer) -> None:
    Order.objects.filter(phone=customer.phone).update(customer=customer)


def edit_customer(customer_id: int, email: str, first_name: str,
                  last_name: str, phone: str, middle_name: str,
                  username: str, birthday: str, password: str) -> None:
    customer = Customer.objects.get(id=customer_id)

    if email:
        customer.email = email

    if first_name:
        customer.first_name = first_name

    if last_name:
        customer.last_name = last_name

    if phone:
        customer.phone = phone

    if middle_name:
        customer.middle_name = middle_name

    if username:
        customer.username = username

    if birthday:
        customer.birthday = datetime.strptime(birthday, '%Y.%m.%d')

    if password:
        customer.set_password(password)

    customer.save()

from main.models import Customer, Order, WorkTask, ProgramPreset, Periphery
from main.serializers.serializers_orders import OrderSerializer, PeripherySerializer


def get_orders(customer: Customer) -> list[dict]:
    return OrderSerializer(customer.orders.all(), many=True).data


def change_order(order_id: int, customer: Customer, **kwargs) -> None:
    order = Order.objects.get(id=order_id, customer=customer)
    if kwargs.get('phone'):
        order.phone = kwargs.get('phone')

    if kwargs.get('price'):
        order.price = kwargs.get('price')

    if kwargs.get('preferences'):
        order.preferences = kwargs.get('preferences')

    if kwargs.get('wishes'):
        order.wishes = kwargs.get('wishes')

    if kwargs.get('call_time'):
        order.call_time = kwargs.get('call_time')

    if kwargs.get('delivery_type'):
        order.delivery_type = kwargs.get('delivery_type')

    if kwargs.get('type'):
        order.type = kwargs.get('type')

    if kwargs.get('status'):
        order.status = kwargs.get('status')

    if kwargs.get('pc_type'):
        order.pc_type = kwargs.get('pc_type')

    if kwargs.get('graphic_card'):
        order.graphic_card = kwargs.get('graphic_card')

    if kwargs.get('processor'):
        order.processor = kwargs.get('processor')

    if kwargs.get('cooling'):
        order.cooling = kwargs.get('cooling')

    if kwargs.get('os'):
        order.os = kwargs.get('os')

    if kwargs.get('setup'):
        order.setup = kwargs.get('setup') == 'true'

    if kwargs.get('tasks'):
        add_order_tasks(order, kwargs.get('tasks'))

    if kwargs.get('presets'):
        add_order_presets(order, kwargs.get('presets'))

    if kwargs.get('peripheries'):
        add_order_peripheries(order, kwargs.get('peripheries'))


def create_order(customer: Customer, **kwargs) -> None:
    order = Order.objects.create(
        customer=customer, phone=kwargs.get('phone'), preferences=kwargs.get('preferences'),
        price=kwargs.get('price'), wishes=kwargs.get('wishes'), call_time=kwargs.get('call_time'),
        delivery_type=kwargs.get('delivery_type'), type=kwargs.get('type'),
        pc_type=kwargs.get('pc_type'), graphic_card=kwargs.get('graphic_card'),
        processor=kwargs.get('processor'), cooling=kwargs.get('cooling'), os=kwargs.get('os'),
        setup=kwargs.get('setup') == 'true', status='received')

    add_order_tasks(order, kwargs.get('tasks'))
    add_order_presets(order, kwargs.get('presets'))
    add_order_peripheries(order, kwargs.get('peripheries'))


def add_order_tasks(order: Order, tasks: []) -> None:
    order.tasks.all().delete()
    [order.tasks.add(WorkTask.objects.get(name=task))
     for task in tasks]


def add_order_presets(order: Order, presets: []) -> None:
    order.presets.all().delete()
    [order.presets.add(ProgramPreset.objects.get(name=preset))
     for preset in presets]


def add_order_peripheries(order: Order, peripheries: []) -> None:
    order.peripheries.all().delete()
    [order.peripheries.add(Periphery.objects.get(name=periphery))
     for periphery in peripheries]


def get_peripheries() -> list[dict]:
    return PeripherySerializer(Periphery.objects.all(), many=True).data

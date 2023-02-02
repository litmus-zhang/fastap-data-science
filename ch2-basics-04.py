def forward_order_status(order):
    if order['status'] == 'new':
        return 'new'
    elif order['status'] == 'in_progress':
        return 'in_progress'
    elif order['status'] == 'complete':
        return 'complete'
    elif order['status'] == 'cancelled':
        return 'cancelled'
    else:
        return 'unknown'
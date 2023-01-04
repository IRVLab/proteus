import proteus_msgs.srv 

def assign_service_type(symbol_input="trigger"):
    if symbol_input == 'trigger':
      return proteus_msgs.srv.SymbolTrigger
    elif symbol_input == 'directional':
        return proteus_msgs.srv.SymbolDirectional
    elif symbol_input == 'target':
        return proteus_msgs.srv.SymbolTarget
    elif symbol_input == 'quantity':
        return proteus_msgs.srv.SymbolQuantity
    else:
        raise ValueError(f"Symbol input type {symbol_input} not recognized")
# app/utils/menu_helper.py (CORREGIDO)

from typing import List, Dict, Optional
# Importar los schemas CORREGIDOS
from app.schemas.menu import MenuItem, MenuResponse
import logging

logger = logging.getLogger(__name__)

def build_menu_tree(menu_items_from_db: List[Dict]) -> List[MenuItem]:
    """
    Construye un árbol de menú jerárquico a partir de una lista plana de items
    obtenida de la base de datos (usando nombres de columna de la tabla 'menu').

    Args:
        menu_items_from_db: Lista de diccionarios con información del menú (resultado del SP corregido).

    Returns:
        List[MenuItem]: Lista de items de menú en estructura jerárquica.
    """
    menu_dict: Dict[int, MenuItem] = {}
    root_items: List[MenuItem] = []

    if not menu_items_from_db:
        logger.warning("build_menu_tree recibió una lista vacía de la base de datos.")
        return []

    # Primero, crear un diccionario de todos los items usando el schema MenuItem corregido
    for item_data in menu_items_from_db:
        try:
            # Asegurarse de que las claves existen antes de accederlas
            # El SP corregido debería devolver estas claves
            menu_id = item_data['menu_id']
            menu_item_obj = MenuItem(
                menu_id=menu_id,
                nombre=item_data.get('nombre', 'Nombre Faltante'), # Usar .get con default
                icono=item_data.get('icono'),
                ruta=item_data.get('ruta'),
                orden=item_data.get('orden'),
                level=item_data.get('Level', 0), # Usar 'Level' como lo devuelve el SP
                es_activo=item_data.get('es_activo', False), # Obtener es_activo
                # --- CORRECCIÓN AQUÍ ---
                area_id=item_data.get('area_id'), # <<< Añadir area_id
                area_nombre=item_data.get('area_nombre'), # <<< Añadir area_nombre
                # --- FIN CORRECCIÓN ---
                children=[]
            )
            menu_dict[menu_id] = menu_item_obj
        except KeyError as e:
            logger.error(f"Falta la clave {e} en los datos del menú: {item_data}")
            # Opcional: saltar este item o lanzar un error
            continue
        except Exception as e:
            logger.error(f"Error procesando item de menú {item_data.get('menu_id', 'ID Desconocido')}: {e}", exc_info=True)
            continue


    # Luego, construir la estructura jerárquica usando 'padre_menu_id'
    for item_data in menu_items_from_db:
        menu_id = item_data.get('menu_id')
        if menu_id not in menu_dict:
             continue # Saltar si hubo error al crear el objeto

        padre_id = item_data.get('padre_menu_id') # Usar la clave correcta

        if padre_id is None:
            # Es un item raíz
            if menu_dict[menu_id] not in root_items: # Evitar duplicados si hay error en datos
                 root_items.append(menu_dict[menu_id])
        else:
            # Es un item hijo, encontrar al padre
            parent = menu_dict.get(padre_id)
            if parent:
                # Añadir el item actual como hijo del padre
                if menu_dict[menu_id] not in parent.children: # Evitar duplicados
                    parent.children.append(menu_dict[menu_id])
            else:
                # Padre no encontrado (podría ser un item huérfano o un error de datos)
                # Podríamos añadirlo a la raíz o registrar un warning
                logger.warning(f"Padre con ID {padre_id} no encontrado para el menú item ID {menu_id}. Añadiendo a la raíz.")
                if menu_dict[menu_id] not in root_items:
                    root_items.append(menu_dict[menu_id])


    # Ordenar los items raíz y los hijos por 'orden'
    # Usar un valor por defecto grande para items sin 'orden' para que vayan al final
    default_order = float('inf')
    root_items.sort(key=lambda x: x.orden if x.orden is not None else default_order)
    for item in menu_dict.values():
        item.children.sort(key=lambda x: x.orden if x.orden is not None else default_order)

    logger.info(f"Árbol de menú construido con {len(root_items)} items raíz.")
    return root_items

def create_menu_response(menu_items_from_db: List[Dict]) -> MenuResponse:
    """
    Crea una respuesta de menú completa usando build_menu_tree corregido.

    Args:
        menu_items_from_db: Lista de diccionarios con información del menú (resultado del SP corregido).

    Returns:
        MenuResponse: Respuesta formateada del menú.
    """
    menu_tree = build_menu_tree(menu_items_from_db)
    return MenuResponse(menu=menu_tree)
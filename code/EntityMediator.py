from code.Bullet import Bullet
from code.Const import WIN_WIDTH
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent,Bullet):
            if ent.rect.right >= WIN_WIDTH:
                ent.health = 0

    #@staticmethod
   # def verify_health(entity_list: list[[Entity]]):
  #
 #       for ent in entity_list:
#            if ent.health <=0:
#                entity_list.remove(ent)
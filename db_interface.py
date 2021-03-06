from abstract_class import AbstractItem
from model_map import db_map


class QueryHandler:
    def create_object(self, obj: AbstractItem):
        parameter_list = dict()
        model_class = obj.model_class
        for field in db_map[model_class]:
            parameter_list[field] = getattr(obj, field)
        model_class = obj.model_class
        for field in db_map[model_class]:
            parameter_list[field] = getattr(obj, field)
        return model_class.create(**parameter_list)

    def retrieve_object(self, obj: AbstractItem):
        parameter_list = dict()
        model_class = obj.model_class
        for field in db_map[model_class]:
            if getattr(obj, field) is not None:
                parameter_list[field] = getattr(obj, field)
        return model_class.select().where(**parameter_list).get()

    def delete_object(self, obj: AbstractItem):
        model_class = obj.model_class
        model_class.delete().where(model_class.id == obj.id)

    def update_object(self, obj: AbstractItem):
        model_class = obj.model_class
        parameter_list = dict()
        for field in db_map[model_class]:
                parameter_list[field] = getattr(obj, field)
        model_class = obj.model_class
        model_class.update(**parameter_list)\
            .where(model_class.id == obj.id).execute()

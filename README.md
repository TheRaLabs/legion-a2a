


to regen specs:

```
cd specs/original/json
datamodel-codegen --input a2a.json --output a2a-dataclass.py --output-model-type dataclasses.dataclass
datamodel-codegen --input a2a.json --output a2a-pydantic-v2.py --output-model-type pydantic_v2.BaseModel

cp a2a-dataclass.py ../../python/datatype/__init__.py
cp a2a-dataclass.py ../../python/pydantic/__init__.py
cd -
```
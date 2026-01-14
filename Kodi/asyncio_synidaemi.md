```python
from time import sleep_ms

def elda(matur, eldunartimi):
    print(f"byrja að elda {matur}")
    sleep_ms(eldunartimi)
    print(f"búið að elda {matur}")
    

def main():
    elda("pizza", 3000)
    elda("pasta", 1500)
    elda("pylsu", 500)
    
main()
```

```python
# samtímakóðavirkni
import asyncio

async def elda(matur, eldunartimi):
    print(f"byrja að elda {matur}")
    await asyncio.sleep_ms(eldunartimi)
    print(f"búið að elda {matur}")
    

async def main():
    asyncio.create_task(elda("pizza", 3000))
    asyncio.create_task(elda("pasta", 1500))
    asyncio.create_task(elda("pylsu", 500))
    while True:
        await asyncio.sleep_ms(1)
    
asyncio.run(main())
```

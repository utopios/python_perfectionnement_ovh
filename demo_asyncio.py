import asyncio

async def tache(nom):
    print(f"{nom} commence")
    await asyncio.sleep(2)
    print(f"{nom} finit")

async def main():
    await asyncio.gather(tache("Tache 1"), tache("Tache 2"))

asyncio.run(main())

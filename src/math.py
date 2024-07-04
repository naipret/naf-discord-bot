import discord


def setup(naf):
    @naf.tree.command(name="add", description="Adds two numbers together.")
    async def add(interaction: discord.Interaction, num1: int, num2: int):
        await interaction.response.send_message(f"{num1} + {num2} = {num1 + num2}")

    @naf.tree.command(name="subtract", description="Subtracts two numbers.")
    async def subtract(interaction: discord.Interaction, num1: int, num2: int):
        await interaction.response.send_message(f"{num1} - {num2} = {num1 - num2}")

    @naf.tree.command(name="multiply", description="Multiplies two numbers.")
    async def multiply(interaction: discord.Interaction, num1: int, num2: int):
        await interaction.response.send_message(f"{num1} * {num2} = {num1 * num2}")

    @naf.tree.command(name="divide", description="Divides two numbers.")
    async def divide(interaction: discord.Interaction, num1: int, num2: int):
        if num2 == 0:
            await interaction.response.send_message("Cannot divide by zero.")
        else:
            await interaction.response.send_message(f"{num1} / {num2} = {num1 / num2}")

    @naf.tree.command(
        name="power", description="Raises one number to the power of another."
    )
    async def power(interaction: discord.Interaction, base: int, exponent: int):
        await interaction.response.send_message(
            f"{base} ^ {exponent} = {base ** exponent}"
        )

    @naf.tree.command(
        name="sqrt", description="Calculates the square root of a number."
    )
    async def sqrt(interaction: discord.Interaction, number: float):
        if number < 0:
            await interaction.response.send_message(
                "Cannot calculate the square root of a negative number."
            )
        else:
            await interaction.response.send_message(f"√{number} = {number ** 0.5}")

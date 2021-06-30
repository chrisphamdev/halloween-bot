import pytest
import discord.ext.test as dpytest


@pytest.mark.asyncio
async def test_ping(bot):
    """ Should fail because a mock_bot has infinite latency which cannot be passed into the f-string."""
    with pytest.raises(Exception) as exception_error:
        await dpytest.message(";ping")
    assert str(exception_error.value) == "Command raised an exception: OverflowError: cannot convert float infinity to integer"

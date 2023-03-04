import logging

logger = logging.getLogger(__name__)


def str_to_bytes32(text):
    assert len(text) <= 32
    text = text + '\0'*(32-len(text))
    return text.encode('utf-8')


def currency_pair_to_pair_id(quote, base):
    return f"{quote}/{base}".upper()


def log_entry(entry, logger=logger):
    logger.info(f"Entry: {entry.serialize()}")


def pair_id_for_asset(asset):
    pair_id = (
        asset["key"] if "key" in asset else currency_pair_to_pair_id(*asset["pair"])
    )
    return pair_id


def key_for_asset(asset):
    return asset["key"] if "key" in asset else currency_pair_to_pair_id(*asset["pair"])

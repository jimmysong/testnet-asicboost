# Analysis of Testnet block version numbers

## Motivation

Recently, it was revealed that Bitmain was testing a version of ASICBoost on testnet. This script tries to find out when and where on testnet blocks this was done.

## How we search

We look for weird version numbers, specifically, ones that aren't repeated more than 5 times total in the entire blockchain. As running the analyze_versions.py shows, most such blocks are around 300900 to 302000.

A similar analysis of the mainnet headers turns up no such blocks with weird version numbers.

## Sources

Data for testnet_blocks comes from http://headers.electrum.org/testnet_headers.
Data for blockchain_blocks comes from http://headers.electrum.org/blockchain_headers.



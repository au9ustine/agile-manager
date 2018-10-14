import requests
import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--key', default=os.environ.get('TRELLO_KEY', ''))
parser.add_argument('--token', default=os.environ.get('TRELLO_TOKEN', ''))
parser.add_argument('--board', default='572ea919522f0bb27fb98d37')
cli_args = parser.parse_args()

TRELLO_API_ENDPOINT_TMPL = 'https://api.trello.com/1/boards/{board_id}'
context = {}
context['key'] = cli_args.key
context['token'] = cli_args.token
board_url = TRELLO_API_ENDPOINT_TMPL.format(
    board_id=cli_args.board,
)


# Establish a connection
def list_cards(board_url, context):
    cards = requests.get('/'.join([board_url, 'cards']), context)
    print(json.dumps(cards.json()))


# Get the board, create a card from template
def create_card(board_url, context):
    pass


# Submit
list_cards(board_url, context)

# References
# - https://developers.trello.com/docs/api-introduction
# - https://developers.trello.com/reference#boards-2

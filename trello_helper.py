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

TITLES_OF_LISTS = [
    "TODO in Sprint 132 (0112-0125)",
    "TODO in Sprint 133 (0126-0208)",
    "TODO in Sprint 134 (0209-0222)",
    "TODO in Sprint 135 (0223-0308)",
    "TODO in Sprint 136 (0309-0322)",
    "TODO in Sprint 137 (0323-0405)",
    "TODO in Sprint 138 (0406-0419)",
    "TODO in Sprint 139 (0420-0503)",
    "TODO in Sprint 140 (0504-0517)",
    "TODO in Sprint 141 (0518-0531)",
    "TODO in Sprint 142 (0601-0614)",
    "TODO in Sprint 143 (0615-0628)",
    "TODO in Sprint 144 (0629-0712)",
    "TODO in Sprint 145 (0713-0726)",
    "TODO in Sprint 146 (0727-0809)",
    "TODO in Sprint 147 (0810-0823)",
    "TODO in Sprint 148 (0824-0906)",
    "TODO in Sprint 149 (0907-0920)",
    "TODO in Sprint 150 (0921-1004)",
    "TODO in Sprint 151 (1005-1018)",
    "TODO in Sprint 152 (1019-1101)",
    "TODO in Sprint 153 (1102-1115)",
    "TODO in Sprint 154 (1116-1129)",
    "TODO in Sprint 155 (1130-1213)",
    "TODO in Sprint 156 (1214-1227)",
    "TODO in Sprint 157 (1228-0110)"
]


# Establish a connection
def list_cards(board_url, context):
    cards = requests.get('/'.join([board_url, 'cards']), context)
    print(json.dumps(cards.json()))


# Get the board, create a card from template
def create_list(board_url, context):
    _list = requests.post('/'.join([board_url, 'lists']), context)
    print(json.dumps(_list.json()))


# Submit
# list_cards(board_url, context)
for title in TITLES_OF_LISTS:
    context['name'] = title
    context['pos'] = 'bottom'
    create_list(board_url, context)

# References
# - https://developers.trello.com/docs/api-introduction
# - https://developers.trello.com/reference#boards-2

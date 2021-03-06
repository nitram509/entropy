#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 syntax=python
#
# Copyright (c) 2006 - 2013 Benjamin Schweizer.
#
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
#

import random
import os

def mkbe850():
    """be850 passwords, entropy = 850 * 899 * 850 = 649,527,500 ~~ 2^29 ~~ 6*10^8"""

    words = [
        # the Basic English vocabulary accordingto C.K. Ogdeni (1930); 850 common words
        'a', 'able', 'about', 'account', 'acid', 'across', 'act', 'addition',
        'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all',
        'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal',
        'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument',
        'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention',
        'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag',
        'balance', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be',
        'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell',
        'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter',
        'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body',
        'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain',
        'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright',
        'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'bulb', 'burn',
        'burst', 'business', 'but', 'butter', 'button', 'by', 'cake', 'camera',
        'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'certain',
        'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest',
        'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth',
        'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come',
        'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex',
        'condition', 'connection', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord',
        'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit',
        'crime', 'cruel', 'crush', 'cry', 'cup', 'current', 'curtain', 'curve',
        'cushion', 'cut', 'damage', 'danger', 'dark', 'daughter', 'day', 'dead',
        'dear', 'death', 'debt', 'decision', 'deep', 'degree', 'delicate', 'dependent',
        'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction',
        'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division',
        'do', 'dog', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress',
        'drink', 'driving', 'drop', 'dry', 'dust', 'ear', 'early', 'earth',
        'east', 'edge', 'education', 'effect', 'egg', 'elastic', 'electric', 'end',
        'engine', 'enough', 'equal', 'error', 'even', 'event', 'ever', 'every',
        'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face',
        'fact', 'fall', 'false', 'family', 'far', 'farm', 'fat', 'father',
        'fear', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field',
        'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame',
        'flat', 'flight', 'floor', 'flower', 'fly', 'fold', 'food', 'foolish',
        'foot', 'for', 'force', 'fork', 'form', 'forward', 'fowl', 'frame',
        'free', 'frequent', 'friend', 'from', 'front', 'fruit', 'full', 'future',
        'garden', 'general', 'get', 'girl', 'give', 'glass', 'glove', 'go',
        'goat', 'gold', 'good', 'government', 'grain', 'grass', 'great', 'green',
        'grey', 'grip', 'group', 'growth', 'guide', 'gun', 'hair', 'hammer',
        'hand', 'hanging', 'happy', 'harbour', 'hard', 'harmony', 'hat', 'hate',
        'have', 'he', 'head', 'healthy', 'hearing', 'heart', 'heat', 'help',
        'here', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn',
        'horse', 'hospital', 'hour', 'house', 'how', 'humour', 'i', 'ice',
        'idea', 'if', 'ill', 'important', 'impulse', 'in', 'increase', 'industry',
        'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'island',
        'jelly', 'jewel', 'join', 'journey', 'judge', 'jump', 'keep', 'kettle',
        'key', 'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge',
        'land', 'language', 'last', 'late', 'laugh', 'law', 'lead', 'leaf',
        'learning', 'leather', 'left', 'leg', 'let', 'letter', 'level', 'library',
        'lift', 'light', 'like', 'limit', 'line', 'linen', 'lip', 'liquid',
        'list', 'little', 'living', 'lock', 'long', 'look', 'loose', 'loss',
        'loud', 'love', 'low', 'machine', 'make', 'male', 'man', 'manager',
        'map', 'mark', 'market', 'married', 'mass', 'match', 'material', 'may',
        'meal', 'measure', 'meat', 'medical', 'meeting', 'memory', 'metal', 'middle',
        'military', 'milk', 'mind', 'mine', 'minute', 'mist', 'mixed', 'money',
        'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth',
        'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation',
        'natural', 'near', 'necessary', 'neck', 'need', 'needle', 'nerve', 'net',
        'new', 'news', 'night', 'no', 'noise', 'normal', 'north', 'nose',
        'not', 'note', 'now', 'number', 'nut', 'observation', 'of', 'off',
        'offer', 'office', 'oil', 'old', 'on', 'only', 'open', 'operation',
        'opinion', 'opposite', 'or', 'orange', 'order', 'organization', 'ornament', 'other',
        'out', 'oven', 'over', 'owner', 'page', 'pain', 'paint', 'paper',
        'parallel', 'parcel', 'part', 'past', 'paste', 'payment', 'peace', 'pen',
        'pencil', 'person', 'physical', 'picture', 'pig', 'pin', 'pipe', 'place',
        'plane', 'plant', 'plate', 'play', 'please', 'pleasure', 'plough', 'pocket',
        'point', 'poison', 'polish', 'political', 'poor', 'porter', 'position', 'possible',
        'pot', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison',
        'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest',
        'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'put', 'quality',
        'question', 'quick', 'quiet', 'quite', 'rail', 'rain', 'range', 'rat',
        'rate', 'ray', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record',
        'red', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect',
        'responsible', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river',
        'road', 'rod', 'roll', 'roof', 'room', 'root', 'rough', 'round',
        'rub', 'rule', 'run', 'sad', 'safe', 'sail', 'salt', 'same',
        'sand', 'say', 'scale', 'school', 'science', 'scissors', 'screw', 'sea',
        'seat', 'second', 'secret', 'secretary', 'see', 'seed', 'seem', 'selection',
        'self', 'send', 'sense', 'separate', 'serious', 'servant', 'sex', 'shade',
        'shake', 'shame', 'sharp', 'sheep', 'shelf', 'ship', 'shirt', 'shock',
        'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple',
        'sister', 'size', 'skin', 'skirt', 'sky', 'sleep', 'slip', 'slope',
        'slow', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake',
        'sneeze', 'snow', 'so', 'soap', 'society', 'sock', 'soft', 'solid',
        'some', 'son', 'song', 'sort', 'sound', 'soup', 'south', 'space',
        'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp',
        'star', 'start', 'statement', 'station', 'steam', 'steel', 'stem', 'step',
        'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone',
        'stop', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'strong',
        'structure', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 'summer', 'sun',
        'support', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take',
        'talk', 'tall', 'taste', 'tax', 'teaching', 'tendency', 'test', 'than',
        'that', 'the', 'then', 'theory', 'there', 'thick', 'thin', 'thing',
        'this', 'though', 'thought', 'thread', 'throat', 'through', 'thumb', 'thunder',
        'ticket', 'tight', 'till', 'time', 'tin', 'tired', 'to', 'toe',
        'together', 'tomorrow', 'tongue', 'tooth', 'top', 'touch', 'town', 'trade',
        'train', 'transport', 'tray', 'tree', 'trick', 'trouble', 'trousers', 'true',
        'turn', 'twist', 'umbrella', 'under', 'unit', 'up', 'use', 'value',
        'verse', 'very', 'vessel', 'view', 'violent', 'voice', 'waiting', 'walk',
        'wall', 'war', 'warm', 'wash', 'waste', 'watch', 'water', 'wave',
        'wax', 'way', 'weather', 'week', 'weight', 'well', 'west', 'wet',
        'wheel', 'when', 'where', 'while', 'whip', 'whistle', 'white', 'who',
        'why', 'wide', 'will', 'wind', 'window', 'wine', 'wing', 'winter',
        'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 'work',
        'worm', 'wound', 'writing', 'wrong', 'year', 'yellow', 'yes', 'yesterday',
        'you', 'young',
    ]

    str = "%s%d%s" % (words[random.randint(0,len(words)-1)], random.randint(100, 999), words[random.randint(0,len(words)-1)])
    return str

def mkalnum54():
    """alnum passwords, entropy = 54^16 = 5,227,573,613,485,916,806,405,226,496 ~~ 2^92 ~~ 5*10^27"""

    chars = '23456789abcdefghjkmnopqrtuvwxyzABCDEFGHJKLMNPQRTUVWXYZ' # not 1ilI 0O sS

    str = ''
    for k in range(16):
        pos = random.randint(0,len(chars)-1)
        str = str + chars[pos]
    return str


def mkalnum84():
    """alphanumeric including special characters, entropy = 84^16 = 6.144.245.739.270.881.311.250.517.590.016 ~~ 2^102 ~~ 6*10^30"""

    chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$\'(){}[]*+,-.<>:;~_' # not url special chars ? % & /
    return "".join([chars[random.randint(0, len(chars) - 1)] for n in range(16)])


def printOneLineWithRenderFunction(headerText, itemRenderFunction):
    """prints a block of passwords with automatic alignment/indentation"""
    text = "" + headerText + "\n"
    text += "".join(["-" for n in headerText]) + "\n"
    numberOfPasswords = 8 * 4
    passwords = [itemRenderFunction() for n in range(numberOfPasswords)]
    maxLength = max([len(word) for word in passwords])
    for i in range(numberOfPasswords):
        text += passwords[i] + "".join([" " for n in range(maxLength - len(passwords[i]))])
        if ((i+1) % 4) == 0:
            text += "\n"
        else:
            text += "  "
    text += "\n"
    return text


def mkbody():
    """render page"""
    result = printOneLineWithRenderFunction("Basic English Passwords (low entropy / e=649,527,500 / 29 bit)", mkbe850)
    result += printOneLineWithRenderFunction("Mixed Alpha Numeric Passwords (high entropy / e=10^27 / 92 bit)", mkalnum54)
    result += printOneLineWithRenderFunction("Alpha,Numeric,Special Passwords (high entropy / e=10^30 / 102 bit)", mkalnum84)
    result += "source code at https://github.com/gopher/entropy"
    return result


def application(environ, start_response):
    """WSGI interface"""
    headers, body, status = {'Content-type': 'text/plain'}, mkbody(), '200 Ok'

    start_response(status, headers.items())
    return [body]

if __name__ == '__main__':
    """CLI+CGI interface"""
    if 'GATEWAY_INTERFACE' in os.environ and os.environ['GATEWAY_INTERFACE'] == 'CGI/1.1':
        print "Content-Type: text/plain"
        print

    # cgi/cli
    print mkbody()

# eof.

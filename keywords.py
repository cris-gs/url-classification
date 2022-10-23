computers_keyword = ['update', 'adapter', 'attached', 'administrator', 'agent', 'algorithm', 'storage', 'speaker', 'antivirus', 'file', 'archive', 'at sign', 'banner', 'bar', 'binary', 'bit', 'binnacle', 'blog', 'bus', 'seeker', 'byte', 'cable', 'cache', 'character', 'binder', 'folder', 'chat', 'chip', 'cyber coffee', 'cybernetics', 'circuit', 'client', 'code', 'command', 'compress', 'computing', 'password', 'controller', 'mail', 'cryptography', 'frame', 'bill', 'depuration', 'developer', 'download', 'digital', 'directory', 'hdd', 'device', 'floppy drive', 'distribution', 'document', 'domain', 'book', 'editor', 'run', 'smiley', 'emulator', 'encrypt', 'link', 'assembler', 'mistake', 'scanner', 'desk', 'standard', 'export', 'extension', 'fiber', 'file', 'firewall', 'signature', 'flow', 'format', 'forum', 'font', 'hacker', 'hardware', 'hyperlink', 'hologram', 'icon', 'to import', 'printing machine', 'wireless', 'intelligence', 'interactive', 'exchange', 'interface', 'internet', 'joystick', 'jumper', 'kernel', 'To be', 'latency', 'reader', 'led', 'language', 'matrix', 'maximize', 'memory', 'menu', 'microprocessor', 'minimize', 'modem', 'module', 'display', 'engine', 'multimedia', 'browser', 'node', 'online', 'computer', 'page', 'screen', 'package', 'flash drive', 'peripheral', 'pixel', 'license plate', 'plugin', 'clipboard', 'laptop', 'processor', 'program', 'programmer', 'protocol', 'port', 'mouse', 'recognition', 'net', 'rendering', 'player', 'request', 'resolution', 'back', 'router', 'security', 'server', 'session', 'simulator', 'system', 'slot', 'overload', 'desktop', 'software', 'spam', 'Tablet', 'card', 'keyboard', 'typography', 'toner', 'transfer', 'unit', 'usability', 'username', 'validation', 'vector', 'window', 'fan', 'video conference', 'virtual', 'virus', 'volume', 'web', 'webmaster', 'wifi', 'plinth']

games_keyword = ['3d', 'abandonware', 'action', 'addiction', 'alpha', 'speakers', 'arcadian', 'art', 'headphones', 'avatar', 'adventure', 'ban', 'beta', 'bonuses', 'boss', 'bot', 'button', 'bug', 'campaign', 'camp', 'cartridge', 'cassette', 'casual', 'cd', 'cheat', 'checkpoint', 'kinematics', 'clan', 'clipping', 'combo', 'computer', 'consumer', 'conversational', 'craft', 'crash', 'test', 'sports', 'developing', 'download', 'discs', 'distributor', 'DVD', 'e sports', 'easter egg', 'electronic', 'emulator', 'energy', 'entertainment', 'strategy', 'expansion', 'fail', 'farm', 'phase', 'fair', 'fps', 'freeware', 'game over', 'game pad', 'gender', 'hardware', 'hype', 'image', 'indie', 'industry', 'instructions', 'artificial intelligence', 'interaction', 'joystick', 'online game', 'kick', 'lag', 'playful', 'manna', 'i send', 'map', 'mmorpg', 'mod', 'currency', 'engine', 'multiplayer', 'rat boy', 'level', 'noob', 'computer', 'lever', 'patch', 'peripheral', 'character', 'perspective', 'platform', 'first person', 'pro gamer', 'mouse', 'virtual reality', 'recreational', 'respawn', 'retro', 'review', 'magazine', 'role', 'scroll', 'sdk', 'shareware', 'shooter', 'simulator', 'skin', 'software', 'sound', 'speed run', 'graphic card', 'keyboard', 'technology', 'tester', 'update', 'extra life', 'walk through', 'youtuber']

valid_url = 0

def search_keywords(keyword):
  keywords = {'computers': {}, 'games': {}}
  if(keyword != 'Invalid url'):
    keyword = keyword.lower()
    total = 0
    for current_keyword in computers_keyword:
      if(current_keyword in keyword):
        total += keyword.count(current_keyword)
        keywords['computers'][current_keyword] = keyword.count(current_keyword)
    keywords['computers']['total'] = total
    total = 0
    for current_keyword in games_keyword:
      if(current_keyword in keyword):
        total += keyword.count(current_keyword)
        keywords['games'][current_keyword] = keyword.count(current_keyword)
    keywords['games']['total'] = total
    return keywords;
  else:
    return {'computers': {'total': 0}, 'games': {'total': 0}};
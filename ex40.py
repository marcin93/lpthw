class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"
		
thing = MyStuff()
thing.apple()
print thing.tangerine

# song singer class
class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def spell_me_a_song(self):
		for i in self.lyrics:
			for j in i:
				print j
			
happy_bday = Song(["\nHappy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["\nThey rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

bulls_on_parade.spell_me_a_song()
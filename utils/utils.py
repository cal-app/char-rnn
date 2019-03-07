import io

def text_cleaner(in_path, charset, out_path):
	with io.open(in_path, encoding='utf-8') as f:
		text = f.read().lower()
		
	textclean = text
	for char in textclean:
		if char not in charset:
			textclean = textclean.replace(char, "")
		
	f = open(out_path,"w") 
	f.write(textclean)
	f.close()
	
	

import sys, string, os

default_dir = "/home/tewson/work/MSc/experiment-2/datasets/"

if len(sys.argv) < 3:
  print "Not enough arguments."

else:
  datacat = sys.argv[1]
  datasrc = sys.argv[2]
  
  filename = default_dir+datacat+"/"+datasrc+".html"
  
  print filename
  
  src = open(filename, "r")
  target = open(filename+".stripjs", "w")
  
  scriptContent = ""
  
  while True:
    pt = src.read(1)
    if(not pt):
      break
    if(pt == '<'):
      #finds a tag
      if(src.read(6) == "script"):
        #finds a script tag
        #reset scriptContent
        scriptContent = ""
        pt = src.read(9)
        while(pt != "</script>"):
          #until it reaches </script>
          src.seek(-8,1)
          scriptContent += pt[0]
          pt = src.read(9)
        
      else:
        target.write(pt)
        src.seek(-6,1)
    else:
      target.write(pt)

  src.close()
  target.close()

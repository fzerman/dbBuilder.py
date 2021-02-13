def get_classes(module):
    clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
    return clsmembers

class StringStructureParser():
    def __init__(self,s,form):
        self.string = s
        self.format = form

    def parse(self):
        self.get_format()
        return self.format_dict

    def get_format_ins_list(self):
        format_ins_list = []

        for i in self.format.split("<"):
            for x in i.split(">"):
                if not x == "":
                    if x == i.split(">")[0]:  
                        format_ins_list.append("<"+x+">")
                    else:
                        format_ins_list.append(x)

        return format_ins_list

    def get_format(self):
        l = self.get_format_ins_list()
        self.format_dict = {}
        self.string_copy = self.string
        for i in l:
            if not( i.startswith("<") and i.endswith(">") ):
                label = l[ l.index(i)-1 ].replace("<","").replace(">","") 
                self.format_dict[ label ] = self.string_copy.partition(i)[0]
                self.string_copy = self.string_copy.partition(i)[2]
            
            #if last index
            if l.index(i) == len(l)-1 and ( i.startswith("<") and i.endswith(">") ):
                label = l[ l.index(i) ].replace("<","").replace(">","") 
                self.format_dict[ label ] = self.string_copy




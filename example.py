
import ipdb

# Relationships.  "has-many" and "belongs-to"

# If an Owner "has-many" Pets, the opposite of this 
# would be a Pet "belongs-to" an Owner

#               Owner ----< Pet
#          "an owner has many pets"

#               Pet >------ Owner
#          "a Pet belongs to an Owner"

# It will ALWAYS be the responsibility of the "belongs to"
# side to know who / what it belongs to.

# If a Pet "belongs to" an Owner, it's the Pet's job to know
# who it belongs to.



class Owner: # an owner has-many Pets
    def __init__( self, name ):
        self.name = name

    def pets( self ):
        final_list = []
        # we need to look through all the pets
        for pet_instance in Pet.all:
        # find those who's owner is equal to self
            if pet_instance.owner == self:
                final_list.append( pet_instance )
        # return a list of only those pets
        return final_list

class Pet: # a pet belongs-to an Owner
    all = []
    def __init__( self, name, age, owner_instance ):
        self.name = name
        self.age = age
        self.owner = owner_instance
        Pet.all.append( self )

o1 = Owner( 'Emiley' )
o2 = Owner( 'Adam' )

p1 = Pet( 'Poppins', 1, o1 )

p2 = Pet( 'Sammy', 6, o2 )
p3 = Pet( 'Luke', 2, o2 )


ipdb.set_trace()
print( 'bye bye' )
class Pet:
    PET_TYPES = [" dog", " cat", " rodent", " bird", " reptile", " exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None): 
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f" Invalid pet type '{pet_type}'. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type

        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet): 
            raise Exception("The pet must be an instance of the Pet class.")
        self.pets.append(pet)
        pet.owner = self
    
    def get_sorted_pets(self): 
        return sorted(self._pets, key=lambda pet: pet.name)


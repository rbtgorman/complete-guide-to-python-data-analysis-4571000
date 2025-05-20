# %% [markdown]
# # 01_05: Data classes

# %%
import math
import collections
import dataclasses
import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# %% [markdown]
# <table>
# <tr><th>name</th><th>lastname</th><th>birthday</th></tr>
# <tr><td>Michele</td><td>Vallisneri</td><td>July 15</td></tr>
# <tr><td>Albert</td><td>Einstein</td><td>March 14</td></tr>
# <tr><td>John</td><td>Lennon</td><td>October 9</td></tr>
# <tr><td>Jocelyn</td><td>Bell Burnell</td><td>July 15</td></tr>
# </table>

# %%
peopledict = [{"name": "Michele", "lastname": "Vallisneri",   "birthday": "July 15"},
              {"name": "Albert",  "lastname": "Einstein",     "birthday": "March 14"},
              {"name": "John",    "lastname": "Lennon",       "birthday": "October 9"},
              {"name": "Jocelyn", "lastname": "Bell Burnell", "birthday": "July 15"}]

# %%
[person for person in peopledict if person["birthday"] == "July 15"]

# %%
Person = collections.namedtuple("Person", ["name", "lastname", "birthday"])

# %%
Person(name='Michele', lastname='Vallisneri', birthday='July 15')

# %%
peopletuples = [Person("Michele", "Vallisneri", "July 15"),
                Person("Albert", "Einstein", "March 14"),
                Person("John", "Lennon", "October 9"),
                Person("Jocelyn", "Bell Burnell", "July 15")]

# %%
[person for person in peopletuples if person.lastname == "Lennon"]

# %%
Person(**peopledict[3])

# %%
peopletuples[3]._asdict()

# %%
@dataclasses.dataclass
class Persondata:
    name: str
    lastname: str
    birthday: str = "unknown"

# %%
peopledata = [Persondata(name="Michele", lastname="Vallisneri", birthday="July 15"),
              Persondata("Albert", "Einstein", "March 14"),
              Persondata("John", "Lennon", "October 9"),
              Persondata("Jocelyn", "Bell Burnell", "July 15")]

# %%
[person for person in peopledata if person.birthday != "July 15"]

# %%
@dataclasses.dataclass
class Persondata:
    name: str
    lastname: str
    birthday: str = "unknown"
    
    # when writing class methods, "self" refers to instances
    def fullname(self):
        return self.name + " " + self.lastname

    # the special method __str__ overrides the standard printout
    def __str__(self):
        return self.lastname + ", " + self.name + ", born " + self.birthday

# %%
michele = Persondata('Michele', 'Vallisneri', 'July 15')

# %%
michele.fullname()

# %%
print(michele)

# %%
@dataclasses.dataclass(frozen = True)
class Persondata_frozen:
    name: str
    lastname: str
    birthday: str = "unknown"


@dataclasses.dataclass(order = True)
class Persondata_ordered:
    name: str
    lastname: str
    birthday: str = "unknown"


@dataclasses.dataclass
class Persondata_customorder:
    name: str
    lastname: str
    birthday: str = "unknown"

    # custom "less than" comparison
    def __lt__(self, other):       
        return (self.lastname, self.name, self.birthday) < (other.lastname, other.name, other.birthday)


@dataclasses.dataclass
class Persondata_computed:
    name: str
    lastname: str
    birthday: str = "unknown"
    fullname: str = dataclasses.field(init=False) # will compute it below

    def __post_init__(self):
        self.fullname = self.name + " " + self.lastname

# %%
import pydantic

# %%
@pydantic.dataclasses.dataclass
class Persondata_pydantic:
    name: str
    lastname: str
    birthday: str = "unknown"

    @pydantic.field_validator("birthday")
    def validate_date(cls, value): # a class method, so first argument is the class 
        
        # will fail if date is not "MONTHNAME DAYNUMBER" 
        datetime.datetime.strptime(value, "%B %d")
        
        return value

# %%
Persondata_pydantic("Michele", 15, "July 15")

# %%
Persondata_pydantic('Michele', "Vallisneri", "7/15")



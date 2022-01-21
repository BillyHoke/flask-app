# PokeDex.GA

PokeDex.GA is an app where users can take a trip down memory lane and browse through Pokedex entries of the original 151 Pokemon. You also have the ability to add up to 6 of your favourite Pokemon to your party and create your own Pokemon Dream Team!

# :grey_question: How to use

-   Sign up with your name, email and password or use the details below -
    - Email = pokedex@ga.com
    - Password = password
-   Browse through the Pokedex entries of the original 151 Pokemon
-   Add up to 6 of your favourite Pokemon to your "party"
-   Change your trainer name to personalise your Pokedex

# :white_check_mark: Live link
https://frozen-spire-76029.herokuapp.com/

# :man_technologist: Technology used
**Languages**
- HTML
- CSS
- Python

**Frameworks**
- Flask
- Jinja2

**Version control**
- Git

**API**
- PokeAPI.com

# :memo: Technical Requirements

Our app must contain the following:

- [x]  **Have at *least* 2 tables** (more if they make sense) – one of them should represent the people using your application (users).
- [x]  **Include sign up/log in functionality (if it makes sense)**, with encrypted passwords & an authorization flow
- [x]  **Modify data in the database** There should be ways for users to add/change some data in the database (it's ok if only admins can make changes).
- [x]  Have **semantically clean HTML and CSS**
- [x]  **Be deployed online** and accessible to the public

# :rage1: Key pain points
Having to rely on the PokeAPI for all of the data in the app was both a good and bad thing. The way it handled height and weight of Pokemon was strange. For every 1 unit in the API it would count as 10kg or 1m. So for instance, Bulbasaur's height in the API was 7 - whilst his actual height is 0.7m. Another example is Charizard who's weight from the API is 905. When in reality his weight is 90.5kg.

In order to get around this I wrote an if statement that would convert the API **int** into a **string**, split that string into an array of individual entries, apply the decimal point to the correct spot and return it back into a **string**. Although there may have been better ways to get the desired result, in the end, I was pleased with how it worked.

```
    if pokemon_weight < 100:
        pokemon_weight = list(str(pokemon_weight))
        pokemon_weight.insert(1, '.')
        pokemon_weight = "".join(pokemon_weight)
    elif pokemon_weight < 999:
        pokemon_weight = list(str(pokemon_weight))
        pokemon_weight.insert(2, '.')
        pokemon_weight = "".join(pokemon_weight)
    elif pokemon_weight < 9999:
        pokemon_weight = list(str(pokemon_weight))
        pokemon_weight.insert(3, '.')
        pokemon_weight = "".join(pokemon_weight)
```

# :bulb: Lessons learned
When naming pages and form actions, take extra care. At the beginning of the project I was careless in my naming conventions and it eventually caught up with me. Once I planned everythig out properly and used the corrent conventions, it all went smoothly.

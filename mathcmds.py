import discord
from discord.ext import commands

# class math_commands(commands.Cog):

#   def __init__(self, bot):
#       self.bot = bot

#   @commands.command(name='math')
#   async def 

async def linear_equations(message):
    embed = discord.Embed()
    embed.title = 'Linear equations'
    embed.color = 0x6ff2e7
    embed.description = 'Try these links:\n1. [Intro to linear equations and inequalities](https://www.khanacademy.org/math/algebra-basics/alg-basics-linear-equations-and-inequalities)\n2. [Solving most and more complex linear equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities)\n3. [Factorising linear equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:intro-factoring/v/factoring-linear-binomials)\n4. [Linear Equations with graphs](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs)\n5. [Different forms of linear equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:forms-of-linear-equations)\n6. [Solving systems of linear equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations)\n7. [Systems and graphs of inequalities](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs)'
    await message.channel.send(embed=embed)
    
async def quadratic_equations(message):
    embed = discord.Embed()
    embed.color = 0x6ff2e7
    embed.title = 'Quadratic equations'
    embed.description = 'Try these links:\n1. [Introduction to quadratics: expanding and factorising](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring)\n2. [Interpreting quadratic graphs](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:intro-parabolas/v/interpret-a-quadratic-graph?modal=0)\n3. [Zero product property](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:factored-form-quadratics/v/zero-product-property?modal=0)\n4. [Factorising quadratics](https://www.khanacademy.org/math/algebra/polynomial-factorization/factoring-polynomials-2-quadratic-forms/e/factoring_polynomials_1)\n5. [Solving by factorisation](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratics-solve-factoring/a/solving-quadratic-equations-by-factoring?modal=0)\n7. [Introduction to vertex form of quadratics](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:vertex-form/v/vertex-form-intro?modal=0)\n8. [Graphing quadratics in vertex form](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:vertex-form/v/graphing-a-parabola-in-vertex-form?modal=0)\n9. [Guide on the quadratic formula](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/a/quadratic-formula-explained-article?modal=0)\n10. [Quadratic equations: the discriminant](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/a/discriminant-review?modal=0)\n11. [Completing the square](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:more-on-completing-square/a/completing-the-square-review?modal=0)'
    await message.channel.send(embed=embed)
  
async def binomial(message):
    embed = discord.Embed()
    embed.color = 0x6ff2e7
    embed.title = 'Binomials'
    embed.description = 'Try these links:\n1. [Introduction to the binomial theorem](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polynomials/x9e81a4f98389efdf:binomial/v/binomial-theorem)\n2. [The binomial distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/v/binomial-distribution)\n3. [The binomial coefficient](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/v/binomial-distribution)\n4. [Binomial expansion using Pascal\'s triangle](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polynomials/x9e81a4f98389efdf:binomial/v/pascals-triangle-binomial-theorem)\n5. [Binomial variables](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/binomial-random-variable/v/binomial-variables)'
    await message.channel.send(embed=embed)
    
async def binomial_theorem(message):
  embed = discord.Embed()
  embed.title = 'Binomial Theorem'
  embed.color = 0x6ff2e7
  embed.set_image(url='https://cdn.discordapp.com/attachments/808105289731407872/808895555303505920/805903287723229294.png')
  embed.description = '[Introduction to the binomial theorem](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polynomials/x9e81a4f98389efdf:binomial/v/binomial-theorem).\n The Binomial Theorem provides us with a way to expand any binomial (a+b) raised to the nth power. Proof of the theorem can be found [here](https://m.youtube.com/watch?v=pam5Edt5nHw).'
  await message.channel.send(embed=embed)
  
async def systems(message):
  embed = discord.Embed()
  embed.title = 'Systems of equations'
  embed.color = 0x6ff2e7
  embed.description = 'Systems of equations are one or more equations used to solve for one or more variable through methods such as elimination and substitution. There must always be at least 2 equations to solve for 2 variables. 3 equations for 3 variables... etc. For more information on a specific method use `-math systems substitution` and `-math systems elimination`.'
  embed.set_image(url='https://media.discordapp.net/attachments/806922774131245109/808974086390808576/805903287723229294.png')
  await message.channel.send(embed=embed)

async def system_substitution(message):
  embed = discord.Embed()
  embed.title = 'Systems of equations using substitution'
  embed.color = 0x6ff2e7
  embed.description = 'Substitution involves making one variable the subject of the equation (isolating it)/\n This means putting it in the form `x = ...` or `y = ...`. We can the substitute the expression on the right hand side of the equals sign into the first equation.\n Depending which variable you isolated you will get a linear equation with just "x" in it or just "y"\n You can solve this last equation to get a value for "x" or "y". Once you have a value for "x" or "y", you can then substitute it in to the other equation to get a linear equation which you can solve to get the value of the other variable.\n\n**Try these links:**\n1. [Solving systems using substitution - Easy](https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-systems-topic/cc-8th-systems-with-substitution/a/systems-of-equations-with-substitution)\n2. [Solving systems using substitution - Full](https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-systems-topic/cc-8th-systems-with-substitution/a/substitution-method-review-systems-of-equations)'
  await message.channel.send(embed=embed)
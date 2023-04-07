import pyvibe as pv

page = pv.Page(title='Daniel Odell', navbar=None)

page.add_header('Daniel Odell')

page.add_text('Theoretical Nuclear Physicist')

'''
Links
'''
links = page.add_card()

links.add_header('Links')

links.add_link('GitHub', 'https://github.com/odell')
links.add_text('I host most of the code for my projects on GitHub. mu2 and \
rose are probably the most user-friendly if you\'re interested in \
checking them out.')

links.add_link('BAND Collaboration', 'https://bandframework.github.io')
links.add_text('''
Check out the exciting work we\'re doing in the Bayesian Analysis of Nuclear
Dynamics collaboration (and the awesome people doing it.
''')

links.add_link('Mastodon', 'https://mastodon.social/@odell')
links.add_text('''
It's unlikely that I've posted anything here, but just in case...
''')


'''
Resume
'''
resume = page.add_card()

resume.add_header('Miniature Resumé')

resume.add_header('History', size=3)
resume.add_text('Postdoctoral Researcher, Ohio University (Current)')
resume.add_text('PhD Theoretical Physics, University of Tennessee (2019)')
resume.add_text('Research Assistant, University of Tennessee (2015)')
resume.add_text('Teaching Assistant, University of Tennessee (2013)')
resume.add_text('Teacher, South Aiken Christian School (2011)')
resume.add_text('Scientist, Savannah River National Laboratory (2007)')
resume.add_text('BS Physics, Clemson University (2007)')

resume.add_header('Selected Publications', size=3)
resume.add_link('19F(p, 𝛾)20Ne | Nature (2022)', 'https://doi.org/10.1038/s41586-022-05230-x')
resume.add_link('BRICK | Frontiers in Physics (2022)', 'https://doi.org/10.3389/fphy.2022.888476')
resume.add_link('t(d,n)𝛼 | Phys. Rev. C (2022)', 'https://doi.org/10.1103/PhysRevC.105.014625')
resume.add_link('van der Waals Effective Field Theory | Phys. Rev. A (2021)',
                'https://doi.org/10.1103/PhysRevA.104.023306')
resume.add_link('Dissertation',
                'https://inspirehep.net/files/415c336f4ff516359dd6bb2c70daa0cb')

with open('index.html', 'w+') as f:
    f.write(page.to_html())

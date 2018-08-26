import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = '__amandinelbe__'
insta_password = 'ficelle123'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_dont_include(['rogissartquentin', 'claaumur', 'dextrocardie', 'violaine_f', 'mayazetoune', 'liamtbrg', 'carochoupinette', 'guigione13', 'friend3', 'baptistekenny',
                              'max_scht', 'lucaaaasgarciarota', 'karakinian', 'cazorlacaroline', 'asolbb', 'lea_gndo', 'aurelkah', 'mado.jc', 'victoireberaud', 'gaelvandecasteele',
                              'clem96e', 'melineboyer', 'mahee_daan', 'antoinens_', 'manukyan_._', 'florent.c83', 'marina.der', 'inesorfeo', 'joanna_bel', 'meloduff', 'myr_oceanne',
                              'k_r_n_m_a', 'lucaas_bernardi13', 'colomet.dielo', 'sourire_a_la_vie_asso'])
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=10000,
				    max_following=4000,
				     min_followers=33,
				      min_following=77)
    session.set_do_comment(True, percentage=30)
    session.set_comments(['Cool !', 'So much fun!!', 'Nicey!', 'Magic', ':)', 'Trop bien =D'])
    session.set_dont_like(['sexy', 'sex', 'porno', 'gore', 'xxx'])

    # actions
    session.like_by_tags(['nature','geographie','velo','voyage','amoureux','gite','ferme','tente', 'foodporn','patisserie','cuisine','restaurant','entreprise','france','animaux',
                          'soleil','valise','bagages','mariage','robe de mariee','decoration','made in france','savon','eurovelo','marseille','combi','box','plamte','ecologie',
                          'durable','paille en bambou','printemps','france','espagne','bicyclette','portugal','homemade','allemagne','belgique','pays-bas','finlande','norvege',
                          'suede','lapponie','lituanie','lettonie','lestonie','grece','pologne','italie','fleur','plante','tombola','association','caritatif','cancer','enfants',
                          'jeunes','lifestyle','boutique','boisson','cocktails','fruits','alcool','charcuterie','fromage','barbecue','brochette','hotel','chambre','bebe','savon','vacances','bougies'], amount=60)

    # default enabled=False, follows ~ 10% of the users from the images, times=1
    # (only follows a user once (if unfollowed again))
    session.set_do_follow(enabled=True, percentage=30, times=2)

    # unfollow users followed by bot
    session.unfollow_users(amount=10, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)


except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()

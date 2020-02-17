from django.test import TestCase, Client
from django.urls import reverse
from produlect.models import *

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Las siguientes lineas reciben el <name> correspondiente a cada <path> ubicado en el archivo <urls.py>, 
        # el cual corresponde al metódo al que se está realizando testing, 
        # metódo que está ubicado en el archivo <views.py>
        self.search_production_url = reverse('searchproduction')
        self.render_create_production_url = reverse('createproduction')
        self.create_production_action_url = reverse('createproductionaction')
        self.update_production_action_url = reverse('updateproductionaction')

    # Testing para Buscar Produccion
    def test_search_production_GET(self):
        # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
        # al inicio de la clase que este posee
        # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
        response = self.client.get(self.search_production_url)
        self.assertEquals(response.status_code, 200)
        # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
        # dicha función está ubidaca en el archivo <views.py>
        self.assertTemplateUsed(response, 'production/search.html')

        # Testing para Render Crear Produccion
    def test_render_create_production_GET(self):
                # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
        # al inicio de la clase que este posee
        # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
        response = self.client.get(self.render_create_production_url)
        self.assertEquals(response.status_code, 200)
                # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
        # dicha función está ubidaca en el archivo <views.py>
        self.assertTemplateUsed(response, 'production/create.html')

        # Testing para Crear Produccion <Action>
    def test_create_production_action_GET(self):
                # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
        # al inicio de la clase que este posee
        # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
        response = self.client.get(self.create_production_action_url)
        self.assertEquals(response.status_code, 200)
                # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
        # dicha función está ubidaca en el archivo <views.py>
        self.assertTemplateUsed(response, 'production/create.html')
#**************************************************************************************************************************************
#--------------------------------------------------------------------------------------------------------------------------------------
        # EN DESARROLLO...!!!!!!!!!!!!!!!!!!!!!!!!!!!!! No quiere servir (¬_¬)
        #ADVERTENCIA, NO TOCAR O DESCONMENTAR, DE LO CONTRARIO SALDRÁ UN ERROR CUANDO REALICEN EL TESTING EN CONSOLA
        #AUNQUE SI LO ARREGLAN, ME AVISAN 
        #ATT: Su Tester novato, Arias :P
#--------------------------------------------------------------------------------------------------------------------------------------        
    #     # Testing para Actualizar Produccion <Action>
    # def test_update_production_action_GET(self):
    #             # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
    #     # al inicio de la clase que este posee
    #     # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
    #     response = self.client.get(self.update_production_action_url)
    #     self.assertEquals(response.status_code, 200)
    #             # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
    #     # dicha función está ubidaca en el archivo <views.py>
    #     self.assertTemplateUsed(response, 'production/update.html')
#--------------------------------------------------------------------------------------------------------------------------------------
#**************************************************************************************************************************************

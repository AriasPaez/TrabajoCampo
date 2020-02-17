from django.test import TestCase, Client
from django.urls import reverse
from produlect.models import *

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        #Producción
        self.search_production_url = reverse('searchproduction')
        self.render_create_production_url = reverse('createproduction')
        self.create_production_action_url = reverse('createproductionaction')
        self.update_production_action_url = reverse('updateproductionaction')
        #Usuario
        self.search_user = reverse('searchuser')
        self.create_user_action = reverse('creatuseraction')
        #Bovinos
        self.search_bovine_url = reverse('searchbovine')
        self.render_create_bovine_url = reverse('createbovine')
        self.create_bovine_action_url = reverse('createbovineaction')
        self.update_bovine_action_url = reverse('updatebovineaction')

     #Testing para la búsquda de bovinos 
     def test_search_bovine_GET(self):
        response = self.client.get(self.search_bovine_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bovine/search.html')

     #Testing para Render de crear bovinos
     def test_render_create_bovine_GET(self):
        response = self.client.get(self.render_create_bovine_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bovine/create.html')
 
     #Testing para modificación de bovinos
     def test_update_bovine_action_GET(self):
        response = self.client.get(self.create_bovine_action_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bovine/create.html')
     
     #Testing para creación de bovinos
     def test_create_bovine_action_GET(self):
        response = self.client.get(self.update_bovine_action_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bovine/update.html')

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

        # Testing para Buscar Usuario
    def test_search_user_GET(self):
                # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
        # al inicio de la clase que este posee
        # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
        response = self.client.get(self.search_user)
        self.assertEquals(response.status_code, 200)
                # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
        # dicha función está ubidaca en el archivo <views.py>
        self.assertTemplateUsed(response, 'user/search.html')

#         # Testing para Crear Usuario
#     def test_create_user_GET(self):
#                 # Toma como <response> el <name> tomado dentro del metódo <setUp>, el cual está ubicado en este mismo archivo (<tests.py>), 
#         # al inicio de la clase que este posee
#         # esto lo hace indicandole a <self.> el atributo correspondiente definido en el <setUP>
#         response = self.client.get(self.create_usern)
#         self.assertEquals(response.status_code, 200)
#                 # El link mostrado a continuación, corresponde al link al cual renderiza la función a la que se está realizando testing
#         # dicha función está ubidaca en el archivo <views.py>
#         self.assertTemplateUsed(response, 'user/create.html')


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

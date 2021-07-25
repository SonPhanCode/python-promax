import os
import time
import playsound
#os.system("color 37")
def bacho():
  print("""























                                                                    WWWW W                                                                                
                                                        Woo-----------o-----oooooooWWWW                                                                 
                                                   Woo-----------ooooooooooWWWWooWWWooWoooooWWWW                                                        
                                              Wo-------ooooooooooWooWWWoooooooooWWWWWooWoooWWoWWWWWWWWW                                                 
                                          oooo--------oooooooooooWooWWWWWWWWWoWWoWWWWWWWWoWWWWoooooooWWoWoo                                             
                                       oooooo------ooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoo---oooWWooW                                         
                                    WWWo-----oooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooo-oooWW                                        
                                 WWWo--------ooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooo-o---oWWW                                      
                               WWWo--------ooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooo-oooooWWW                                   
                               WWo------ooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooo--o-oWWWWW                                 
                             WWoo------oooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooo---ooW WWW                                
                            WWW-------ooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooo-oooWWWWW                                
                           WWoW------ooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooo--oWoWWWW                                
                           WWWo-------ooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooo--ooWWWWW                                
                          WWWooo-------ooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooo----oWWWWW                               
                          WWW-o-------ooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooo----oWWWW                             
                         WWWoo-------oooooooooooooooo-ooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooWWWWWoooo- --oWWW                               
                         WWo----o-----ooooooooo--ooo------------oooWWWWWWWWWWWWWWWWWWWWWoooooooooooWWWWooooWWWoooo--- -oW                               
                           o--------oooooooooo----oo-oooWooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooWoWooo--- oWW                              
                            oo-o--oooooooooooooooooooWWWWWWWWWWWWoooooWWWWWWWWWWWWWWWooWWWWWWWWWWWWWWWWWWWWoooWWWoo--oooW                               
                          --ooo------ooooooooooooooooWWWWWWWWooooWWWoooooWWWWWWWWWWoooWWWo-------  -oWWWoWoWWWWWWWo---WWoW                              
                           oooooo---ooooooooooooooo----------------oooooooWWWWWWWWWooooo--oW-----ooooo---ooWWWWWWoooooWWWWW                             
                           WWooWoo--ooooooooooooo-oooooooWWooWoooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooWWWWW                             
                          WooooWWo---ooooooooooooWooooWWWWWWWWWWWWWWWooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooWWWoWWW                            
                          ooooWWooo--ooooooooooWWWWWWWoooooooooWWWWWWooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooWWoWWWW                            
                          oooWoooWWo-ooooooooooWWWWWWWWWWWWWWWWWWWWWWoooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooW ooWWWW                            
                          oooWWooWWWo--oooooooWWWWWWWWWWWWWWWWWWWWWWWooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooWoWWWWW                             
                           WoooWWoooo----ooooooWWWWWWWWWWWWWWWWWWWoooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooWWWWWWWW                             
                            WoWWWWoooo----ooooooWWWWWWWWWWWWWWWWoooooWWWWWWWW W  WWWWWWWWWWooWWWWWWWWWWWWWWWWWWWoooWWWWWWW                              
                              WWWWWWWoW----ooooooooWWWWWWWWWWooooooooWWWWooWWWWWWWWWWWWWWWWWWooooWWWWWWWWWWWWWWWooWWWWWWW                               
                               WoWWWoWoo-ooooooooooooooWWoooooWWWo--oooo-oo-------------oWWWWWWWooooWWWWWWWWooWWWoW  oW                                 
                                  Wooo  W-oooooooooooooooooooWWWWWWWooooWoooWWWWWWoWWWWWWWWWWWWWWWWWWWWWWooWWWWWWo                                      
                                         oooooooooooooooooooooWoooWoWWW oooWooo-ooWW ooWWW WWWWWWWWWWWWWWWWWWWWWWW                                      
                                          oooooooooooooooWoWWWWoo--oWoooo-W---oo-ooWoWoWooWooWoW   WWWWWWWWWWWWWW                                       
                                          Woooooooooooo  WoWoo----o--------o----o-oo--o---------WW   WWWWWWWWWWo                                        
                                           WoooooooooW  oWoo---oo-o--oooWWoooooWWoooooooWWWWWoo-oWWW  WWWWWWWooW                                        
                                             oooooWoo WWoooo-oWWoooooooooooooooooWWWoWWoWoWWWWoWW W    WWWWWooW                                         
                                               oooooW WWo-oWoooooooo----------o---ooooWooWWWWWWWWW   WWWWWWWoW                                          
                                                 oooW Wo-oWWWooooooooooooW WoWW WooWWWWWWWW W WWWW WWWWWWWWWWo                                          
                                                   ooWWo-oooWoooooooWWW WooWoWWWWoWWWWWWWW WW WW  WWWWWWWWWWo                                           
                                                     oooo-ooooooooooooWW  oWWWWW WWWWWWWWWWWWWW WWooooWWWWWW                                            
                                                    ooooooooooooooWoWW  W  WW WW oWWooWWWWoWWWWWoWooWWWWWW                                              
                                                   Wo--ooo-oooWWWW  WWWWWWWWW W  W  oWoWWW WWWoWoooWoWoW                                                 
                                                 WWW----oooWoWWW W WWWWWWWWWWWWW W W WWoWW  oWo-oWooooW                                                    
                                              WWWWWW--o-oWWoWWW W WWWWWWWWWWWWWWWWWW  WooW WW WoooooW                                                        
                                     WWWWWWWWWWWW WWo-ooWoW WWWWo WWWWWWWWWWWWWWWWWWW oWW ooW W WWoW                         W                                  
                            WWWWWWWWWWWWWWWW  WWW WWWWoooWW WWWWW oWWIIIIII W W W  oWooWW W  WW  W  W    W           WW                                   
                  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W WWWWWoWW WWWWo-W IIIIII Wo WW WoooWWW          W                 WW                                   
           WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWW oWoWWWWWWWWW W WWWoWoo WoWoooWW W W  W                  W                                      
     WWWWWWWWWWWW WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWo-ooWoWWWWWWWW oWoW W WWW-Wo--o oWWoooW W WWW           W                                              
    WWWWWWWWWWW   WWWWWWWWWWWWWWWWWWW   WWWWWoW-------o-ooWWW WWWWWW ooWWW-ooooWooW-oWoW            W                                                   
    WWWWWWWWWWW     WWWWWWWWWWWWWWWWWWWWWWWW o------oWWWWooWooWWWW W WW  WooooWWWW-oWoWWW           WWW  W                                              
    WWWWWWWW         WWWWWWWWWWWWW W WWWWW --------WWWWWWWWWWWWWWWWoWoWWoWWWWoWWWoooWWo W      WWWWW WW   W WW                                          
    WW WWWWW        WWWWWWWWWWW  W WWW o------oWWWWWWWWWWWW WWWWWWoo-ooWoW---ooWWWWoWWooW WWWWW      WWWW    W """)
def bando():
  print("""











                                                                                                                                            
                                                                   o                                                                        
                                                     o   o o o o-o----o-o-                                                                  
                                                    --oooo----------------                                                                  
                                                      oo---o-------------oo-o                                                               
                                                        -o---o-o---------o---o o                                                            
                                                               o-o-o----o-                                                                  
                                                                 o--oooo                                                                    
                                                             o---o-o--                                                                      
                                                               o-ooo-  o                 --o----                                            
                                                                  oo-oo                   -o- o                                             
                                                                     --o- o                                                                 
                                                                        -o-o                                                                
                                                                         o-o--o                                                             
                                                                             -----                                                          
                                                                              oo--oo                                                        
                                                                              -o-----                                                       
                                                                              --------                                                      
                                                                              -o------             o-o--- o                                 
                                                                              oo-------                                                     
                                                                              o-----o- -                                                    
                                                                          oo-o--------                                                      
                                                                      -o-oo----------o                                                      
                                                                  ----oo-o-----o-                                                           
                                                                --ooooooo-o                                                                 
                                                                 -oo------               --                                                 
                                                                 -o--        o--          o                                                 
                                                                 o           --o                                                            
                                                                                                                                            

  """)
def co():
  print("""  




                                   ###    -           --                                                                                                                                                     
                                    ##           -         ---------------------               --------------------------------                                                                              
                                    ###            -------           ------------------------             -----------------------------------              ---------   ---                                   
                                     ###   --  --        --------            ------------------------------------      ----------------------------------      -----------                                   
                                  --  ##  -- - ------------ ------------            ------------------      -----------------      --------------------------------  ----                                    
                                   --  ##- ----    ----------------------------           -------------------       -------------------      -------------------------------                                 
                                    -  ###  ---- -         --------------------------           ---------------------      --------------------      -------------------------                               
                                    --  ##- -- - -------         ---------------------------          ----------------   ---      ---------------------      -----------------                               
                                  -   ##- ---- -----------        -----------------------------          ----------    ---------     ------------------------       -------                               
                                  ---  ## -  --- ---------------         -----------------------------         -----      --------------    -----------------------------                                  
                                       -  ##- --------------------------        ------------------------------       -        -------------------   -------------------------------                          
                                     ---   ##- ---- --    -------------------         -----------------------------             -----------------------   --------------------------                         
                                     -----  ## - -- - -----    --------------------         --------                                              ------------  ---------------------                         
                                   --------  ##------- --------     ---------------------        ---------                                    ---------------------- ----------------                         
                                 ---------   ##     ---------------     ----------------------       ---------                            ------------------------------ -----------                         
                                 ----------  ##   -  -------------------    ----------------------       -----------                    ----- ------------------------------- ------                         
                                  ---------   ##- --  ----------------------    -----------------------      -------                      --------- -----------------------------  --                        
                                 -----------   # - -  ------------------------------------------------------     ---                       --------------------------------------------                      
                                 ------------   #      ----------------------------------------------------------            -------         --------------------------------------------                    
                                 ------------   ##-     ------------------------------------------------------------      ----------------     -------------------------------------------                   
                                  ---------- -   #       ----------------------------------------------------------    -    -------------------  -------------------------------------------                 
                                  ---------- -   #      ---------------------------------------------------------- --------   --------------------------------------------------------------                
                                     ------  -    #  -    ----------------------------------------------------------------------  ------------------------------------------------------------               
                                       -----   -   #       ---------------------------------- ------------------------------------------------------------------------------------------------               
                                         ----      ##      ------------------------------------------------------------------------------------------------------------------------------------              
                                          --        ##      -----------------------------------------------------------------------------------------------------------------------------------              
                                                     #      -------------------------------------------------------------------------------------------------------------   ------                           
                                                      #      ---------------------------------------------------------------------------------------                                                         
                                                       #       -------------------------------------------------------------                                                                                  
                                                        #      ---------------------------------------------------                                                                                            
                                                         #      ------------------------------                                                                                                                
                                                          #       ----------------                                                                                                                             
                                                           #      --""")
def co1():
  print("""



















  
                                          --ooooooooooo-                                                                             -ooooooooooo--                                                     
                                ooooooooooooooooooooooooooooo--                                                           -oooooooooooooooooooooooooooooo                                             
  ---------------------oooooooooooooooooooooooooooooooooooooooooooooo-                                            -ooooooooooooooooooooooooooooooooooooooooooooo-                                     
  ooo-oooo-o-o-o--oooooooooooooooooooooooooooooooooooooooooooooooooooo------                                ------ooooooooooooooooooooooooooooooooooooooooooooooo------                               
  oooooo--o--o-oooooooooooooooooooooooooooooooooooooooooooooooooooooooo-------------                --------------ooooooooooooooooooooooooooooooooooooooooooooooo--------------               ------  
  oooooo-ooooooo-ooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------  
  ooooo---ooo-oooo-ooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------   
  oooooo-oo-oo-oooo-oooooooooooooooooooooooooooooooooooooooooooooooo-o-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------   
  oooooo---o-oooo-ooooooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------   
  ooooooo-o--ooo--oooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------   
  ooooooooo--ooo-ooooooooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo------------------------------------   
  ooooooo-o-oo----oooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------   
  ooooooooo--ooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------   
  oooooo-oo-ooo-oooooooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------ooo---------ooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------   
  ooooooo--oo--ooooooooooooooooooooooooooooooooooooooooooooooooooooo------------------------------ooooo---------oooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------oooooooo-------oooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------oooooooooo----ooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo----------------------------ooooooooooooo---ooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------oooooooooooooooW--oooWWWWWWWWWWWWWWWooooooooooooooooooooooooooooo-------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooWWoo--------------------------ooooooooooooooooWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooooooooo-------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooWWWooooooo---------------oooooooooooooooooooWWWWWWWWWWWWWWWooooooooooooooooooooooooooooooooo--------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooWoooooooooooooooooooooooooooooooooooooooWWWWWWWWWWWWWWWoooooooooooooooooooooooooooooooooo---------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-o--oooooooooooooooooooooooooooooooooooooooWWWWWWWWWWWWoooooooooooooooooooooooooooooooooooo---------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo------oooooooooooooooooooooooooooooooooooooWWWWWWWWWWoooooooooooooooooooooooooooooooooooooo---------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo---------ooooooooooooooooooooooooooooooooWWWWWWWWWWoooooooooooooooooooooooooooooooooooooooo---------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo------------oooooooooooooooooooooooooooooWWWWWWWWWoooooooooooooooooooooooooooooooooooooooo----------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------ooooooooooooooooooooooooooooWWWWWWWWWooooooooooooooooooooooooooooooooooooooo----------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------ooooooooooooooooooooooooWWWWWWWWWWooooooooooooooooooooooooooooooooooooooo----------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-------------------oooooooooooooooooooooooWWWWWWWWWWWoooooooooooooooooooooooooooooooooooooo----------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo------------------ooooooooooooooooooooooooWWWWWWWWWWWooooooooooooooooooooooooooooooooooooo-----------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------oooooooooooooooooooooooooWWWWWWWWWWWWooooooooooooooooooooooooooooooooooooo----------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------oooooooooooooooooo---ooooWWWWWWWWWWWWooooooooooooooooooooooooooooooooooooo----------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo----------------oooooooooooooooo-----------ooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-----------------ooooooooooooo--------------oooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo----------------ooooooooo------------------oooooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------   
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo----------------oooo------------------------oooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------   
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------    
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------    
  oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------    
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------    
  ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo------------------------------------------    
  oooooooooooooooooooooooooo-                     -oooooooooo--------------------------------------------oooooooooo-                         ooooooooooo------------------------------------------    
  ooooooooooooooooo--                                    -oo---------------------------------------------oo-                                       -ooo-------------------------------------------    
                                                               --------------------------------------                                                     --------------------------------------      
                                                                       ----------------------                                                                     ----------------------              """)
def co2():
  print("""



















  
                                                            WWWWW                                                                                     oWWWW                                              
                                                 ooooooooooooooooooooooooooo                                                               ooooooooooooooooooooooooooo                                   
                                         -ooooooooooooooooooooooooooooooooooooooooo                                                -ooooooooooooooooooooooooooooooooooooooooo-                           
   ooo-------------------  -------------ooooooooooooooooooooooooooooooooooooooooooooo-----                                  ------ooooooooooooooooooooooooooooooooooooooooooooo------                    
   --oo---------------------------------oooooooooooooooooooooooooooooooooooooooooooo--------------                  --------------oooooooooooooooooooooooooooooooooooooooooooo--------------             
   oooo--------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   oo-oo--o-----------------------------ooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   oo---ooo----------------------------o-ooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   oo---------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   o--oo-------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   o-oo--oo---------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   oo-o------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-----------------------    
   -----------------------------------oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------    
   oo-o------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo-------------------------    
   -oo-o-----------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------oooo-------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------    
   ----o----------------------------oooooooooooooooooooooooooooooooooooooooooooooo----------------oooooo-----------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------------------    
   ---oo-----------------------------oooooooooooooooooooooooooooooooooooooooooooo---------------oooooooooo---------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------------------    
   -----o----------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------ooooooooooooo--------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------------------    
   -o-o---o-------------------------oooooooooooooooooooooooooWWWWWWWWWWWWWooooooo-----------ooooooooooooooooo------------------oooooooooooooooooooooooooooooooooooooooooooo--------------------------    
   o----o---------------------------ooooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWooo----ooooooooooooooooooooo----------------oooWWWooooooooooooooooooooooooooooooooooooooo--------------------------    
   -o------------------------------ooooooooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWoooooooooooooooooooooooooooo---ooooooooWWWWWWWooooooooooooooooooooooooooooooooooooooooo--------------------------    
   o-----o------------------------oooooooooooooooooooooooooooooooooooWWWWWWWWWWWWWWWoooooooooooooooooooooooooooooooooooooooWWWWWoooooooooooooooooooooooooooooooooooooooooo---------------------------    
   ooooo---o-----------------------oooooooooooooooooooooooooooooooooooooWWWWWWWWWWWWoooooooooooooooooooooooooooooooooooooooWWWooooooooooooooooooooooooooooooooooooooooooooo--------------------------    
   --oo---------------------------ooooooooooooooooooooooooooooooooooooooooWWWWWWWWWoooooooooooooooooooooooooooooooooooooooWWoooooooooooooooooooooooooooooooooooooooooooooo---------------------------    
   o-oo-o-------------------------ooooooooooooooooooooooooooooooooooooooooooWWWWWWWoooooooooooooooooooooooooooooooooooooooo--ooooooooooooooooooooooooooooooooooooooooooooo---------------------------    
   --o-oo------------------------ooooooooooooooooooooooooooooooooooooooooooooooWWWooooooooooooooooooooooooooooooooooooooo----ooooooooooooooooooooooooooooooooooooooooooooo---------------------------    
   oo-----------------------------oooooooooooooooooooooooooooooooooooooooooooooooWooooooooooooooooooooooooooooooooooooo------oooooooooooooooooooooooooooooooooooooooooooo----------------------------    
   ooo---------------------------oooooooooooooooooooooooooooooooooooooooooooooooWWoooooooooooooooooooooooooooooooooooo-------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------    
   oo-o--------------------------ooooooooooooooooooooooooooooooooooooooooooooooWWWooooooooooooooooooooooooooooooooooooo-----ooooooooooooooooooooooooooooooooooooooooooooo----------------------------    
   ---o-------------------------oooooooooooooooooooooooooooooooooooooooooooooooWWWooooooooooooooooooooooooooooooooooooo-----ooooooooooooooooooooooooooooooooooooooooooooo----------------------------    
   ----o------------------------ooooooooooooooooooooooooooooooooooooooooooooooWWWoooooooooooooooooooooooooooooooooooooo-----ooooooooooooooooooooooooooooooooooooooooooooo----------------------------    
   ooo--------------------------oooooooooooooooooooooooooooooooooooooooooooooWWWWooooooooooooooooooooooooooooooooooooooo----oooooooooooooooooooooooooooooooooooooooooooo-----------------------------    
   o-oo-------------------------oooooooooooooooooooooooooooooooooooooooooooooWWWWooooooooooooooooooooooooooooooooooooooo---ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------    
   o--o-------------------------ooooooooooooooooooooooooooooooooooooooooooooWWWWoooooooooooooooo-----------oooooooooooooo--ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------    
   -o-o---o---------------------ooooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------ooo--ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------    
   oo--o-----------------------oooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------    
   ----o----------------------ooooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------------    
   -oo-------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------------    
   --oooo----------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------------    
   o---oo----------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------------------------    
   oo----o-------------------ooooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------------------------    
   o-ooo---------------------o-ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo-------------------------------    
   -o-o----------------------oooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------------------------    
   ---o---o------------------ooooooooooooooo-                -ooooooooooooo----------------------------------------------ooooooooooooo-                -oooooooooooooo-------------------------------    
   --o----------------------oooooooo-                                -ooooo---------------------------------------------oooooo-                                -ooooo--------------------------------    
            ---------------                                                 -------------------------------------------                                               -------------------------------    
                                                                                  ------------------------------                                                             ------------------------    
                                                                                            -----------                                                                               -----------       """)
def co3():
  print("""





















                            -oooooooooooooo-                                                                   -oooooooooooooooooooooo-                                                                
                   -ooooooooooooooooooooooooooooooo-                                                   --oooooooooooooooooooooooooooooooooooo-                                                         
  --oo-oo-ooooooooooooooooooooooooooooooooooooooooooooo---                                       ---ooooooooooooooooooooooooooooooooooooooooooooo----                                      ----oo-     
  -oo-----oooooooooooooooooooooooooooooooooooooooooooo-----------                        -----------ooooooooooooooooooooooooooooooooooooooooooooo-----------                        -----------oo-     
  --oo-o--oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oo-     
  o-oooo--oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------oo-     
  oo---o--ooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oo-     
  o--o--o-ooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooo-     
  ooo-o-oo--ooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooo-     
  --oo-oooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooo     
  oo-oo--oooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------oooo     
  --ooo---oooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oWoooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooo     
  --ooooo--ooooooooooooooooooooooooooooooooooooooooo--------------------------------------------oWWWWoooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooo     
  -o--ooo-oooooooooooooooooooooooooooooooooooooooooo-------------------------------------------oWWWWWWWooooooooooooooooooooooooooooooooooooooo-----------------------------------------------oooo      
  oo--o-o-oooooooooooooooooooooooooooooooooooooooooo------------------------------------------WWWWWWWWWWoooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooo      
  oo-o----ooooooooooooooooooooooooooooooooooooooooo------------------------------------------ooWWWWWWWWWWWoooooooooooooooooooooooooooooooooooo----------------------------------------------ooooo      
  oo--oo-oooooooooooooooooooooooooooooooooooooooooo----------------------------------------oooWWWWWWWWWWWWWoooWWWWWWWWWooooooooooooooooooooooo----------------------------------------------ooooo      
  ---o--o-o-ooooooooooooooooooooooooooooooooooooooo----------------------------------------oooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooooo----------------------------------------------ooooo      
  oo-o--ooooooooooooooooooooooooooooooooooooooooooo--------------------------------------ooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooo----------------------------------------------oooooo      
  oo--o--ooooooooooooooooooooooooooooooooooooooooo-------------------------------------oooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooo----------------------------------------------oooooo      
  o-o-o---oooooooooooooooooooooooooooooooooooooooo--------------------------------ooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooo----------------------------------------------oooooo      
  -o--o-o-oooooooooooooooooooooooooooooooooooooooo---------------oooooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooo-----------------------------------------------ooooo      
  o----ooooooooooooooooooooooooooooooooooooooooooo------------------oooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooo----------------------------------------------oooooo      
  --oo---oooooooooooooooooooooooooooooooooooooooo----------------------oooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooooo-----------------------------------------------oooooo      
  -o-----oooooooooooooooooooooooooooooooooooooooo-------------------------ooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooooo----------------------------------------------ooooooo      
  -----o-oooooooooooooooooooooooooooooooooooooooo----------------------------oooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooo----------------------------------------------ooooooo      
  -oo-----o-ooooooooooooooooooooooooooooooooooooo--------------------------------ooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooo----------------------------------------------ooooooo      
  ------ooooo-oooooooooooooooooooooooooooooooooo----------------------------------oooooooooWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooo-----------------------------------------------ooooooo      
  ----oo--oooooooooooooooooooooooooooooooooooooo----------------------------------ooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooo----------------------------------------------oooooooo      
  -ooo----oooooooooooooooooooooooooooooooooooooo---------------------------------ooooooooooWWWWWoooooooWWWWWWWWWWWWWWoooooooooooooooooooooo----------------------------------------------oooooooo      
  --------oooooooooooooooooooooooooooooooooooooo---------------------------------ooooooooooWWooooooooooooooooooooWWWWoooooooooooooooooooooo----------------------------------------------oooooooo      
  -----o--oooooooooooooooooooooooooooooooooooooo--------------------------------ooooooooooo---oooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------oooooooo      
  -o-ooo-oo-oooooooooooooooooooooooooooooooooooo--------------------------------oooooooo------oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooo      
  -o----ooooooooooooooooooooooooooooooooooooooo--------------------------------oooooo---------oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooo      
  oo--o-ooooooooooooooooooooooooooooooooooooooo--------------------------------ooo-----------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooo       
  ---o----oooooooooooooooooooooooooooooooooooo-----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooo       
  -o--o--oooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooo       
  o----o-ooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooo       
  -oo----ooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooo       
  o----o--oooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------ooooooooo       
  ------oooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo-----------------------------------------------ooooooooo       
  oo-oo--oo-ooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooo       
  o--o-oooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooo  -       -  oooooooooooooooo----------------------------------------------oooooooooo       
  -o--o---ooooooooooooooo            oooooooo----------------------------------------------ooooooo                              -ooooooo----------------------------------------------ooooooo          
  oooooooo                                  o----------------------------------------------                                            -----------------------------------------------                 
                                                    --------------------------------                                                          --------------------------------                         
                                                           ----------------                                                                           ----------------                                """)
def co4():
  print("""



















  
                                                                      Wooooooooooooo -                                                                           oooooooooooooo                          
                                                              ooooooooooooooooooooooooooooooo                                                           -oooooooooooooooooooooooooooooo-                 
   oo-oooooo-                                         oooooooooooooooooooooooooooooooooooooooooooooo                                            -oooooooooooooooooooooooooooooooooooooooooooooo          
   ooooo--o--------------                      -------ooooooooooooooooooooooooooooooooooooooooooooo--------                              --------ooooooooooooooooooooooooooooooooooooooooooooo-----      
   -oooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------              ----------------ooooooooooooooooooooooooooooooooooooooooooooo-----      
   oo-ooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo------      
   ooo---o-o------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-----      
   -oooooo-o------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------      
   ooooo-o--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------      
   oo-oo--o-------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo------      
   ooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------      
   oo-oo-oo-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooWo-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo--------     
   oo-o----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooWWWWWo------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo--------     
   -oooo--------------------------------------------oooooooooooooooooooooooooooooooooooooooooWWWWWWWooo----------------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------     
   o---oo-------------------------------------------oooooooooooooooooooooooooooooooooooooooWWWWWWWWWoooo--------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------     
   o-o---------------------------------------------ooooooooooooooooooooooooooooooooooooooWWWWWWWWWWWooooo--------------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------     
   ooo---o-----------------------------------------oooooooooooooooooooooooooooooooooooWWWWWWWWWWWWWWoooooo------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------     
   o-o---------------------------------------------oooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooo----------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------     
   oo-o--------------------------------------------ooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooo---------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------     
   o-oooo------------------------------------------oooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooo------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------     
   -o-oo-------------------------------------------oooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooo-----------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------     
   -o----------------------------------------------ooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooooooooooooo-------ooooooooooooooooooooooooooooooooooooooooooooo----------     
   -o-oo--o---------------------------------------ooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooooooooooooo---------oooooooooooooooooooooooooooooooooooooooooooo-----------     
   -o-o-------------------------------------------oooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooooooooooo----------ooooooooooooooooooooooooooooooooooooooooooooo-----------     
   -o---------------------------------------------oooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooooooooo------------ooooooooooooooooooooooooooooooooooooooooooooo-----------     
   -ooo------------------------------------------oooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooooooooo--------------ooooooooooooooooooooooooooooooooooooooooooooo-----------     
   ooo----o--------------------------------------oooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooooo-----------------oooooooooooooooooooooooooooooooooooooooooooo-------------    
   o--oo----------------------------------------o-oooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooo------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------    
   o--o--o--------------------------------------oooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWooooooooooooooooooooooo--------------------ooooooooooooooooooooooooooooooooooooooooooooo------------    
   -o--o----------------------------------------ooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooo------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------    
   ooooo-oo-------------------------------------ooooooooooooooooooooooooooWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooooooooooo------------------ooooooooooooooooooooooooooooooooooooooooooooo-------------    
   -o-oo----------------------------------------oooooooooooooooooooooooooWWWooooooooooooooooo--------oooooooooooooooooooo-----------------oooooooooooooooooooooooooooooooooooooooooooooo-------------    
   o-oo---o-------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo------------ooooooooooooooooo----------------oooooooooooooooooooooooooooooooooooooooooooooo-------------    
   -o----o--------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------ooooooooooooo----------------oooooooooooooooooooooooooooooooooooooooooooooo-------------    
   o--o-----------------------------------------oooooooooooooooooooooooooooooooooooooooooooo----------------------ooooooooo---------------ooooooooooooooooooooooooooooooooooooooooooooo--------------    
   -oooo---------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------ooo---------------oooooooooooooooooooooooooooooooooooooooooooo---------------    
   -o-------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------    
   o-ooo-o------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------    
   oooo---------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooo---------------    
   -o-o-o-------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------    
   oo--o--------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------------    
   -ooo---------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------------    
   o-o-o--------------------------------------oooooooooooooooooooooooooooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooo----------------    
   -o-oo-o-----------------------------------oooooooooooo                      oooooooooooo---------------------------------------------ooooooooooo                      -ooooooooooo----------------    
   o---oo------------------------------------ooo-                                     -ooo---------------------------------------------oooo                                      oooo----------------    
                  ------------------------                                                   ----------------------------------------                                                  --------------    
                                                                                                    -------------------------                                                                  ------   """)
def co5():
  print("""




















                                                                                                     WWWWW                                                                                             
                                                                                        ooooooooooooooooooooooooooo                                                               oooooooooooooo     
                oo----------o                                                   -ooooooooooooooooooooooooooooooooooooooooo-                                               o-oooooooooooooooooooo     
    ooooooooooooooooooooooooooooo------                                  -----oooooooooooooooooooooooooooooooooooooooooooooooo---                                  -----oooooooooooooooooooooooo     
    oooooooooooooooooooooooooooo--------------                   -------------oooooooooooooooooooooooooooooooooooooooooooooo-------------                  -------------oooooooooooooooooooooooo     
    oooo--ooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooo     
    oooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooo     
    oooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------oooooooooooooooooooooooo     
    oooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooo     
    ooooooooooooooooooooooooooo-o-------------------------------------------ooooooooooooooooooooWoooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooo     
    oooooooooooooooooooooooooo-----------------------------------------------oooooooooooooooooWWWWWoooooooooooooooooooooooo-------------------------------------------oooooooooooooooooooooooooo     
    ooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooooWWWWWWWoooooooooooooooooooooo--------------------------------------------oooooooooooooooooooooooooo     
    ooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooWWWWWWWWWWoooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooo     
    ooooooooooooooooooooooooooo---------------------------------------------oooooooooooooooWWWWWWWWWWWWooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooo     
    ooooooooooooooooooooooooo-o--------------------------------------------ooooooooooooooWWWWWWWWWWWWWWWWooooooooooooooooo--------------------------------------------oooooooooooooooooooooooooo     
    ooooooooooooooooooooooooo----------------------------------------------oooooooooooooWWWWWWWWWWWWWWWWWWoooooooooooooooo--------------------------------------------oooooooooooooooooooooooooo     
    oooooooooooooooooooooooooo---------------------------------------------ooooooooooooWWWWWWWWWWWWWWWWWWWWWooooooooooooo---------------------------------------------oooooooooooooooooooooooooo     
    ooooooooooooooooooooooooo----------------------------------------------ooooooooooWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooo--------------------------------------------oooooooooooooooooooooooooo     
    ooooooooooooooooooooooooo----------------------------------------------oooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooo--------------------------------------------ooooooooooooooooooooooooooo     
    ooooooooooooooooooooooooo---------------------------------------------oWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWo-------------------------------------------ooooooooooooooooooooooooooo     
    oooooooooooooooooooooooo-----------------------------------------oooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooo-------------------------------------oooooooooooooooooooooooooooo     
    oooooooooooooooooooooooo-------------------------------------ooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooo-------------------------------oooooooooooooooooooooooooooo     
    oooooooooooooooooooooooo-----------------------------------------ooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooooooooooooooo--------------------------oooooooooooooooooooooooooooo     
    oooooooooooooooooooooooo---------------------------------------------oWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooooooooooo-------------------------------oooooooooooooooooooooooooooo     
    ooooooooooooooooooooooo----------------------------------------------ooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWoooo--------------------------------------ooooooooooooooooooooooooooooo    
    oooooooooooooooooooooo-----------------------------------------------oooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWooo-------------------------------------------oooooooooooooooooooooooooooooo    
    ooooooooooooooooooooooo----------------------------------------------ooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWo----------------------------------------------ooooooooooooooooooooooooooooo    
    oooooooooooooooooooooooo-------------------------------------------o-ooooooWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWo--------------------------------------------oooooooooooooooooooooooooooooo    
    oooooooooooooooooooooo---------------------------------------------oooooooWWWWWWWWWWWWWWWWoooooWWWWWWWWWWWWWWWWWWWWo-------------------------------------------oooooooooooooooooooooooooooooo    
    oooooooooooo----ooooooo---------------------------------------------ooooooWWWWWWWWWWWooooooooooooooWWWWWWWWWWWWWWWWo------------------------------------------ooooooooooooooooooooooooooooooo    
    oooooooooooooooooo-ooo---------------------------------------------ooooooWWWWWWWWooooooooooooooooooooooWWWWWWWWWWWWW-----------------------------------------oooooooooooooooooooooooooooooooo    
    oooooooooooooooo-oooo----------------------------------------------ooooooWWWWWoooooooooooooooooooooooooooooWWWWWWWWWo-----------------------------------------ooooooooooooooooooooooooooooooo    
    oooooooooooooooooooo----------------------------------------------oooooooWWoooooooooooooooooooooooooooooooooooWWWWWWoo---------------------------------------oooooooooooooooooooooooooooooooo    
    ooooooooooooooooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooooWooo---------------------------------------ooooooooooooooooooooooooooooooo-    
    oooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo---ooo--------------------------------------ooooooooooooooooooooooooooooooo-    
    oooooooooooooooooooo-o--------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------ooooooooooooooooooooooooooooooo-    
    oooooooooooooooooooo----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooo-    
    ooooooooooooooooooo-----------------------------------------------ooooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooo-    
    oooooooooooo-ooooooo----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooo    
    ooooooooooooooooooooo---------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooo    
    ooooooooooooooooooo-----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo--------------------------------------------ooooooooooooooooooooooooooooooooo    
    ooooooooooooooooooo-o--------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo---------------------------------------------ooooooooooooooooooooooooooooooooo    
    oooooooooooooooooo-----------------------------------------------oooooooooooooooooooooooooooooooooooooooooooooo-------------------------------------------o-ooooooooooooooooooooooooooooooooo    
    oooooooooooooooooo-o--------------------------------------------ooooooooooooo                      oooooooooooo-------------------------------------------ooooooooooooo                          
    ooooooooooooooooooo---------------------------------------------ooooo                                     -oooo--------------------------------------------oooo-                                 
                          ----------------------------------------                                                   ----------------------------------------                                        
                                  ------------------------                                                                  -------------------------                                                
""")
def vn():
  print("""




















                @@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@@@          
                 @@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@                   @@@@@@@@@@@@@             
                   @@@@@@@@@@@                      @@@@@@@@@@             @@@@@@@@@@@@@@@                   @@@@@@@@                 
                   @@@@@@@@@@                      @@@@@@@@               @@@@@@@@@@@@@@@@@                 @@@@@@@@                  
                   @@@@@@@@@@                    @@@@@@@@                @@@@@@@@@@@@@@@@@@@               @@@@@@@@                   
                   @@@@@@@@@@                  @@@@@@@@                 @@@@@@@@ @@@@@@@@@@@              @@@@@@@@                    
                   @@@@@@@@@@                @@@@@@@@                  @@@@@@@@   @@@@@@@@@@@            @@@@@@@@                     
                   @@@@@@@@@               @@@@@@@@                   @@@@@@@@     @@@@@@@@@@@          @@@@@@@@                      
                  @@@@@@@@@@             @@@@@@@                     @@@@@@@@       @@@@@@@@@@@        @@@@@@@@                       
                  @@@@@@@@@@           @@@@@@@                      @@@@@@@@         @@@@@@@@@@@      @@@@@@@@                        
                  @@@@@@@@@@         @@@@@@@                       @@@@@@@@          @@@@@@@@@@@     @@@@@@@@                         
                  @@@@@@@@@        @@@@@@@                        @@@@@@@@            @@@@@@@@@@@   @@@@@@@@                          
                  @@@@@@@@@      @@@@@@                          @@@@@@@@              @@@@@@@@@@@ @@@@@@@@                           
                  @@@@@@@@@    @@@@@@                           @@@@@@@@                @@@@@@@@@@@@@@@@@@                            
                  @@@@@@@@@  @@@@@@                            @@@@@@@@                 @@@@@@@@@@@@@@@@@                             
                  @@@@@@@@@@@@@@@                             @@@@@@@@                   @@@@@@@@@@@@@@@                              
                 @@@@@@@@@@@@@                               @@@@@@@                      @@@@@@@@@@@@                                
                 @@@@@@@@@@@                               @@@@@@@@@                       @@@@@@@@@@                                 
                 @@@@@@@@@                            @@@@@@@@@@@@@@@@@                     @@@@@@@@                                  
""")
def main():
  i=0
  while i<1:
    bacho()
    time.sleep(2)
    os.system("cls")
    co()
    time.sleep(2)
    os.system("cls")
    bando()
    time.sleep(2)
    os.system("cls")
    vn()
    time.sleep(2)
    os.system("cls")
    i+=1
  os.system("color 07")
  while True:
    co1()
    time.sleep(0.3)
    os.system("cls")
    co2()
    time.sleep(0.3)
    os.system("cls")
    co3()
    time.sleep(0.3)
    os.system("cls")
    co4()
    time.sleep(0.3)
    os.system("cls")
    co5()
    time.sleep(0.3)
    os.system("cls")
main()


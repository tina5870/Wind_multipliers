"""
 Author: Tina Yang, tina.yang@ga.gov.au 
 CreationDate: 2014-05-01
 Description: Engineered data used to test topographic multiplier computation 
 Version: $Rev$ 
 $Id$
"""

import numpy as np


test_slope = dict([(1, 0),
                   (2, 0.049),
                   (3, 0.05),
                   (4, 0.051),
                   (5, 0.1),
                   (6, 0.2),
                   (7, 0.44),
                   (8, 0.45),
                   (9, 0.46),
                   (10, 0.7),
                   (11, 0.8),
                   (12, 0.9),
                   (13, 1.0),
                   (14, 1.5),
                   (15, 0),
                   (16, 0.049), 
                   (17, 0.05),
                   (18, 0.051),
                   (19, 0.1),  
                   (20, 0.2), 
                   (21, 0.44),
                   (22, 0.45),
                   (23, 0.46),
                   (24, 0.7),
                   (25, 0.8),
                   (26, 0.9),
                   (27, 1.0),              
                   (28, 1.5)])



test_escarp = dict([(1, 'Y'),
                    (2, 'Y'),
                    (3, 'Y'),
                    (4, 'Y'),
                    (5, 'Y'),
                    (6, 'Y'),
                    (7, 'Y'),
                    (8, 'Y'),
                    (9, 'Y'),
                    (10, 'Y'),
                    (11, 'Y'),
                    (12, 'Y'),
                    (13, 'Y'),
                    (14, 'Y'),
                    (15, 'N'),
                    (16, 'N'), 
                    (17, 'N'),
                    (18, 'N'),
                    (19, 'N'),  
                    (20, 'N'), 
                    (21, 'N'),
                    (22, 'N'),
                    (23, 'N'),
                    (24, 'N'),
                    (25, 'N'),
                    (26, 'N'),
                    (27, 'N'),              
                    (28, 'N')])
               
               
mh_engineered = dict([(1, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.])),
                      (2, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.])),
                      (3, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.01,1.02,1.02,1.03,1.03,1.04,1.04,1.05,1.05,\
                                    1.06,1.06,1.07,1.08,1.07,1.07,1.07,1.07,1.06,1.06,\
                                    1.06,1.06,1.06,1.05,1.05,1.05,1.03,1.,1.,1.])),
                      (4, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.01,1.02,1.02,1.03,1.03,1.04,1.04,1.05,1.06,\
                                    1.06,1.07,1.07,1.08,1.07,1.07,1.07,1.07,1.07,1.06,\
                                    1.06,1.06,1.06,1.06,1.05,1.05,1.03,1.,1.,1.])),
                      (5, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.10,1.11,\
                                    1.12,1.13,1.14,1.15,1.15,1.14,1.14,1.13,1.13,1.13,\
                                    1.12,1.12,1.11,1.11,1.10,1.10,1.07,1.,1.,1.])),
                      (6, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.01,\
                                    1.03,1.05,1.07,1.09,1.11,1.13,1.15,1.18,1.20,1.22,\
                                    1.24,1.26,1.28,1.30,1.29,1.28,1.28,1.27,1.26,1.25,\
                                    1.24,1.23,1.23,1.22,1.21,1.20,1.13,1.,1.,1.])),
                      (7, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.02,\
                                    1.06,1.11,1.16,1.20,1.25,1.29,1.34,1.39,1.43,1.48,\
                                    1.52,1.57,1.62,1.66,1.64,1.62,1.61,1.59,1.57,1.55,\
                                    1.53,1.51,1.50,1.48,1.46,1.44,1.29,1.,1.,1.])),
                      (8, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.02,\
                                    1.07,1.11,1.16,1.21,1.25,1.30,1.35,1.39,1.44,1.49,\
                                    1.54,1.58,1.63,1.68,1.66,1.64,1.62,1.60,1.58,1.56,\
                                    1.55,1.53,1.51,1.49,1.47,1.45,1.30,1.,1.,1.])),
                      (9, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.03,\
                                    1.08,1.13,1.17,1.22,1.26,1.31,1.36,1.40,1.45,1.49,\
                                    1.54,1.59,1.63,1.71,1.69,1.67,1.62,1.60,1.59,1.57,\
                                    1.55,1.53,1.51,1.49,1.47,1.46,1.31,1.,1.,1.])),
                      (10, np.array([1.,1.,1.,1.,1.,1.,1.07,1.20,1.23,1.26,\
                                    1.29,1.32,1.35,1.38,1.41,1.44,1.47,1.50,1.54,1.57,\
                                    1.60,1.63,1.66,1.71,1.70,1.68,1.67,1.64,1.63,1.62,\
                                    1.60,1.59,1.58,1.57,1.55,1.54,1.44,1.20,1.,1.])),
                      (11, np.array([1.,1.,1.,1.,1.,1.,1.15,1.26,1.29,1.31,\
                                    1.34,1.37,1.40,1.42,1.45,1.48,1.50,1.53,1.56,1.58,\
                                    1.61,1.64,1.67,1.71,1.70,1.69,1.68,1.65,1.64,1.63,\
                                    1.62,1.61,1.60,1.58,1.57,1.56,1.48,1.26,1.04,1.])),
                      (12, np.array([1.,1.,1.,1.,1.,1.02,1.21,1.31,1.33,1.36,\
                                    1.38,1.41,1.43,1.45,1.48,1.50,1.53,1.55,1.57,1.60,\
                                    1.62,1.65,1.67,1.71,1.70,1.69,1.68,1.67,1.65,1.64,\
                                    1.63,1.62,1.61,1.60,1.59,1.58,1.50,1.31,1.12,1.])),
                      (13, np.array([1.,1.,1.,1.04,1.07,1.09,1.26,1.35,1.37,1.39,\
                                    1.41,1.44,1.46,1.48,1.50,1.52,1.54,1.57,1.59,1.61,\
                                    1.63,1.65,1.68,1.71,1.70,1.69,1.68,1.67,1.65,1.64,\
                                    1.64,1.63,1.62,1.61,1.60,1.59,1.52,1.35,1.17,1.])),
                      (14, np.array([1.,1.,1.12,1.26,1.28,1.29,1.41,1.47,1.48,1.50,\
                                    1.51,1.53,1.54,1.56,1.57,1.59,1.60,1.61,1.63,1.64,\
                                    1.66,1.67,1.69,1.71,1.70,1.70,1.69,1.69,1.68,1.67,\
                                    1.67,1.66,1.65,1.64,1.64,1.63,1.59,1.47,1.35,1.])),
                      (15, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.])),
                      (16, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.,1.,1.,1.,1.,1.,1.,1.,1.,1.])), 
                      (17, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.01,1.02,1.02,1.03,1.03,1.04,1.04,1.05,1.05,\
                                    1.06,1.06,1.07,1.08,1.07,1.06,1.06,1.05,1.05,1.04,\
                                    1.04,1.03,1.03,1.02,1.02,1.01,1.,1.,1.,1.])),
                      (18, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.01,1.02,1.02,1.03,1.03,1.04,1.04,1.05,1.06,\
                                    1.06,1.07,1.07,1.08,1.07,1.07,1.06,1.06,1.05,1.04,\
                                    1.04,1.03,1.03,1.02,1.02,1.01,1.,1.,1.,1.])),
                      (19, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,\
                                    1.01,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.10,1.11,\
                                    1.12,1.13,1.14,1.15,1.14,1.13,1.12,1.11,1.10,1.09,\
                                    1.08,1.07,1.06,1.05,1.04,1.03,1.,1.,1.,1.])),  
                      (20, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.01,\
                                    1.03,1.05,1.07,1.09,1.11,1.13,1.15,1.18,1.20,1.22,\
                                    1.24,1.26,1.28,1.30,1.28,1.26,1.24,1.22,1.20,1.18,\
                                    1.15,1.13,1.11,1.09,1.07,1.05,1.,1.,1.,1.])), 
                      (21, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.02,\
                                    1.06,1.11,1.16,1.20,1.25,1.29,1.34,1.39,1.43,1.48,\
                                    1.52,1.57,1.62,1.66,1.62,1.57,1.52,1.48,1.43,1.39,\
                                    1.34,1.29,1.25,1.20,1.16,1.11,1.,1.,1.,1.])),
                      (22, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.02,\
                                    1.07,1.11,1.16,1.21,1.25,1.30,1.35,1.39,1.44,1.49,\
                                    1.54,1.58,1.63,1.68,1.63,1.58,1.54,1.49,1.44,1.39,\
                                    1.35,1.30,1.25,1.21,1.16,1.11,1.,1.,1.,1.])),
                      (23, np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.03,\
                                    1.08,1.13,1.17,1.22,1.26,1.31,1.36,1.40,1.45,1.49,\
                                    1.54,1.59,1.63,1.71,1.66,1.61,1.54,1.49,1.45,1.40,\
                                    1.36,1.31,1.26,1.22,1.17,1.13,1.,1.,1.,1.])),
                      (24, np.array([1.,1.,1.,1.,1.,1.,1.07,1.20,1.23,1.26,\
                                    1.29,1.32,1.35,1.38,1.41,1.44,1.47,1.50,1.54,1.57,\
                                    1.60,1.63,1.66,1.71,1.68,1.65,1.61,1.57,1.54,1.50,\
                                    1.47,1.44,1.41,1.38,1.35,1.32,1.07,1.,1.,1.])),
                      (25, np.array([1.,1.,1.,1.,1.,1.,1.15,1.26,1.29,1.31,\
                                    1.34,1.37,1.40,1.42,1.45,1.48,1.50,1.53,1.56,1.58,\
                                    1.61,1.64,1.67,1.71,1.68,1.65,1.63,1.58,1.56,1.53,\
                                    1.50,1.48,1.45,1.42,1.40,1.37,1.15,1.,1.,1.])),
                      (26, np.array([1.,1.,1.,1.,1.,1.02,1.21,1.31,1.33,1.36,\
                                    1.38,1.41,1.43,1.45,1.48,1.50,1.53,1.55,1.57,1.60,\
                                    1.62,1.65,1.67,1.71,1.69,1.66,1.64,1.61,1.57,1.55,\
                                    1.53,1.50,1.48,1.45,1.43,1.41,1.21,1.,1.,1.])),
                      (27, np.array([1.,1.,1.,1.04,1.07,1.09,1.26,1.35,1.37,1.39,\
                                    1.41,1.44,1.46,1.48,1.50,1.52,1.54,1.57,1.59,1.61,\
                                    1.63,1.65,1.68,1.71,1.69,1.67,1.64,1.62,1.59,1.57,\
                                    1.54,1.52,1.50,1.48,1.46,1.44,1.26,1.,1.,1.])),              
                      (28, np.array([1.,1.,1.12,1.26,1.28,1.29,1.41,1.47,1.48,1.50,\
                                    1.51,1.53,1.54,1.56,1.57,1.59,1.60,1.61,1.63,1.64,\
                                    1.66,1.67,1.69,1.71,1.70,1.68,1.67,1.65,1.64,1.62,\
                                    1.61,1.59,1.57,1.56,1.54,1.53,1.41,1.12,1.,1.]))])

#elevation along the line, used in test_findpeaks.py
test_line = dict([(1, np.array([0,0,0,0,0,0,0,0,0,0,\
                                0,0,0,0,0,0,0,20,20,20,\
                                20,25,30,35,40,45,50,55,60,65,\
                                70,75,80,85,90,95,100,105,110,115,\
                                120,122,124,126,128,130,132,134,136,138,\
                                140,142,144,146,148,150,152,154,156,158,\
                                160,168,176,184,192,200,208,216,224,232,\
                                240,248,256,264,272,280,288,296,304,312,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,315,310,305,300,295,290,285,280,275,\
                                270,265,260,255,250,245,240,235,230,225,\
                                220,212.5,205,197.5,190,182.5,175,167.5,160,152.5,\
                                145,137.5,130,122.5,115,107.5,100,92.5,85,77.5,\
                                70,70,70,70,70,70,70,70,70,70,\
                                70,70,70,70,70,70,70,70,70,70,\
                                70,70,70,70,70,70,70,70,70,70,\
                                70])),
                  (2, np.array([0,0,0,0,0,0,0,0,0,0,\
                                0,0,0,0,0,0,0,20,20,20,\
                                20,25,30,35,40,45,50,55,60,65,\
                                70,75,80,85,90,95,100,105,110,115,\
                                120,122,124,126,128,130,132,134,136,138,\
                                140,142,144,146,148,150,152,154,156,158,\
                                160,168,176,184,192,200,208,216,224,232,\
                                240,248,256,264,272,280,288,296,304,312,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320])),
                  (3, np.array([0,0,0,0,0,0,0,0,0,0,\
                                0,0,0,0,0,0,0,20,20,20,\
                                20,25,30,35,40,45,50,55,60,65,\
                                70,75,80,85,90,95,100,105,110,115,\
                                120,140,140,140,128,130,132,134,136,138,\
                                140,142,144,146,148,150,152,154,156,158,\
                                160,168,176,184,192,200,208,216,224,232,\
                                240,248,256,264,272,280,288,296,304,312,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320,320,320,320,320,320,320,320,320,320,\
                                320]))])
                                

expect_hill_no = dict([(1, 1),
                       (2, 2),                                
                       (3, 3)])
                      
expect_height = dict([(1, 300),
                      (2, 300),                                
                      (3, 300)])
                      
                      
expect_slope = dict([(1, 0.2),
                     (2, 0.2),                                
                     (3, 0.2)])     
                     
expect_downwind_slope = dict([(1, 0.33),
                              (2, 0.),                                
                              (3, 0.)]) 
                              
expect_escarpment_factor = dict([(1, 1.0),
                                 (2, 0.),                                
                                 (3, 0.)])   
                                 
                                 
# ideal results from Martin, ignoring the small hills                                 
#expect_results = dict([(1, [1, 300, 0.2, 0.33, 1.0]),
#                       (2, [2, 300, 0.2, 0, 0]),                                
#                       (3, [3, 300, 0.2, 0, 0])])                                  
                       
# scripts derived results, including small hills
expect_results = dict([(1, [2, 20, 300, 0.83, 0.2, 999, 0.17, 1.0, 1.25]),
                       (2, [2, 20, 300, 0.83, 0.2, 999, 0, 1.0, 2.5]),                                
                       (3, [3, 20, 120, 192, 0.83, 0.23, 0.21, 999, -0.06, 0, 1, 2.87, 2.5])]) 
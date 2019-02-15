/*
 * gpio.h
 *
 *  Created on: Aug 17, 2017
 *      Author: Mohamed
 */

#ifndef HAL_GPIO_H_
#define HAL_GPIO_H_
/* ========================================================================== */
/*                             Include Files                                  */
/* ========================================================================== */
#include "../HAL/gpio_hw.h"
#include "../HAL/hw_types.h"
#include "../HAL/types.h"
#ifdef __cplusplus
extern "C" {
#endif
/* ========================================================================== */
/*                           Macros & Typedefs                                */
/* ========================================================================== */

/****************************************************************************************************
* Field Definition pins Macros
****************************************************************************************************/
#define 					pin0                   0
#define 					pin1               	   1
#define 					pin2                   2
#define 					pin3                   3
#define 					pin4                   4
#define 					pin5                   5
#define 					pin6                   6

/* ========================================================================== */
/*                           Structures and Enums                             */
/* ========================================================================== */

/** \brief Enumerate the types of errors in the gpio module.*/
typedef enum {
	PASS , INCORRECT_PORT , INCORRECT_PIN_NUM , DIRECTION_ERROR ,
	INCORRECT_MASK , INCORRECT_VALUE , INCORRECT_INTERRUPT_SENSE
}gGPIOError_t;
/** \brief enum holding the GPIO direction register context. */
typedef enum gpioDirection
{
	 INPUT    ,
	 GPIO_DIRECTION_INPUT = 0 , /

 	/**< Input pin. */
	 GPIO_DIRECTION_OUTPUT  ,
	 OUTPUT = 1 ,
	/**< Output pin. */
}gpioDirection_t;

typedef enum gpioOutput
{
	GPIO_OUTPUT_LOW = LOW ,
	/** \brief GPIO pin is at logic low.*/
	GPIO_OUTPUT_HIGH = HIGH,
	/** \brief GPIO pin is at logic high.*/
}gpioOutput_t;



typedef enum gpioEnable
{
	ENABLE = 1 , enable = 1 , Enable = 1,
	/** \brief GPIO pin is at logic low.*/
	DISABLE = 0 , Disable = 0 , disable = 0
	/** \brief GPIO pin is at logic high.*/
}gpioEnable_t;



typedef enum gpioDigitalEn
{
	GPIO_DIGITAL_LOW ,
	/** \brief GPIO pin is at logic low.*/
	GPIO_DIGITAL_HIGH ,
	/** \brief GPIO pin is at logic high.*/
}gpioDigitalEn_t;


typedef enum gpioPort
{
	PORTA , porta =0 , PA =0 , pa =0 ,
	PORTB , portb =1 , PB =1 , pb =1 ,
	PORTC , portc =2 , PC =2 , pc =2 ,
	PORTD , portd =3 , PD =3 , pd =3 ,
	PORTE , porte =4 , PE =4 , pe =4 ,
	PORTF , portf =5 , PF =5 , pf =5 ,
}gpioPort_t;


typedef enum gpioPcm
{
	pcm0 , PCM0 =0 ,
	pcm1 , PCM1 =1 ,
	pcm2 , PCM2 =2 ,
	pcm3 , PCM3 =3 ,
	pcm4 , PCM4 =4 ,
	pcm5 , PCM5 =5 ,
	pcm6 , PCM6 =6 ,
}gpioPcm_t;


/** \brief Enumerates the possible GPIO Resistor type . */
typedef enum restype
{
	PULLUP , PULLDOWN , OPENDRAIN
}gpioResType_t;

/** \brief Enumerates the possible GPIO Current Value  . */

typedef enum currentval
{
	CURRENT_2MA , CURRENT_4MA , CURRENT_8MA
}gpioCurrentVal_t;

/** \brief Enumerates the possible GPIO Interrupt Sens  . */

typedef enum intSens
{
	GPIO_INTERRUPT_EDGE ,EGDE= 0,
	GPIO_INTERRUPT_LEVEL ,LEVEL = 1 ,
}gpioIntSens_t;

/** \brief Enumerates the possible GPIO Interrupt Both Edges . */

typedef enum intIbe
{
	GPIO_INTERRUPT_EVENT   ,
	GPIO_INTERRUPT_SINGLE_EDGE = 0 ,
	GPIO_INTERRUPT_BOTH_EDGES
}gpioIntIbe_t;

/** \brief Enumerates the possible GPIO Interrupt Event type . */

typedef enum intIev
{
	GPIO_INTERRUPT_EDGE_FALLING ,
	GPIO_INTERRUPT_LEVEL_LOW =0  ,
	GPIO_INTERRUPT_EDGE_RISING  ,
	GPIO_INTERRUPT_LEVEL_HIGH= 1
}gpioIntIev_t;

/** \brief Enumerates the possible GPIO Interrupt Masked pin . */

typedef enum intIm
{
	MASKED , UNMASKED
}gpioIntIm_t;

/** \brief Enumerates the possible GPIO Interrupt  Clear . */

typedef enum intClear
{
	CLEAR = 1
}gpioIntClear_t;

/** \brief Structure holding the GPIO configration context. */
typedef struct gpioPinConfig
{
	gpioDirection_t gpio_dir ;
	/**< GPIO Direction register value. */
	gpioOutput_t gpio_output ;
	/**< GPIO Data register value. */
	gpioDigitalEn_t gpio_digital_enable ;
	/**< GPIO Digital Enable register value. */
	gpioResType_t gpio_resistor_type ;
	/**< GPIO Resistor type for selected pin . */
	gpioCurrentVal_t gpio_current_val ;
	/**< GPIO Current value to source from register value. */
	gpioGeneralStatus_t gpio_alternative_function_select ;
	/**< GPIO Alternative Function register value. */
	gpioGeneralStatus_t gpio_commit;
	/**< GPIO Commit register value for selected pin*/
	uint8_t gpio_port_control ;
	/**< GPIO Port control MUX number for selected pin register value. */
	gpioGeneralStatus_t gpio_analog_digital_converver_control;
	/**< GPIO Analog Digital Converter register value. */
	gpioGeneralStatus_t gpio_direct_access_memory_control ;
	/**< GPIO Direct Access Memory register value. */

}gpioPinConfig_t;





/* ========================================================================== */
/*                           Variables Declarations                           */
/* ========================================================================== */

/*   None  */

/* ========================================================================== */
/*                           Function Declarations                            */
/* ========================================================================== */










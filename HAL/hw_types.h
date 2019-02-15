/*
 * hw_types.h
 *
 *  Created on: feb 12, 2019
 *      Author: kotoz
 */

#ifndef HW_TYPES_H_
#define HW_TYPES_H_
/* ========================================================================== */
/*                             Include Files                                  */
/* ========================================================================== */
#include "types.h"
#ifdef __cplusplus
extern "C" {
#endif
/* ========================================================================== */
/*                           Macros & Typedefs                                */
/* ========================================================================== */
#ifndef INPUT
#define INPUT 0
#endif

#ifndef OUTPUT
#define OUTPUT 1
#endif

#ifndef LOW
#define LOW 0
#endif

#ifndef HIGH
#define HIGH 1
#endif
/* ========================================================================== */
/*                           Structures and Enums                             */
/* ========================================================================== */


/* ========================================================================== */
/*                           Variables Declarations                           */
/* ========================================================================== */




/* ========================================================================== */
/*                           Function Declarations                            */
/* ========================================================================== */
	/**
 *
 *  \brief  Macro to read a 32 bit register.
 *
 *  \param  address  32bit register address.
 *
 */
static inline uint32_t HW_READ_REG32(uint32_t reg);
/**
 *
 *  \brief  Macro to write a value to a 32 bit register.
 *
 *  \param  address  32bit register address.
 *  \param  value    value to write to the 32bit register.
 *
 */

static inline void HW_WRITE_REG32(uint32_t reg,
								   uint32_t value);
/**
 *
 *  \brief  Macro to set a bit in a 32bit register.
 *
 *  \param  addr  32bit register address.
 *  \param  bit   the bit number to be set.
 *
 */
static inline void HW_SET_BIT(uint32_t reg,
								     uint32_t bit);

/**
 *
 *  \brief  Macro to reset a 32 bit register.
 *
 *  \param  reg  32bit register address.
 *  \param  bit   the bit number to be reset.
 *
 */

static inline void HW_CLEAR_BIT(uint32_t reg,
								       uint32_t bit);

static inline void HW_TOGGLE_BIT(uint32_t reg,
								        uint32_t bit);

static inline uint32_t HW_READ_BIT(uint32_t reg,
								       uint32_t bit);

/**
 *
 *  \brief  Macro to read a 32 bit register software masked.
 *
 *  \param  addr   32bit register address.
 *  \param  value  value to be written.
 *  \param  mask   the required mask.
 *
 *  \details This function is used to write values to a specific number of bits
 *           and lets the other bits unchanged.
 *           This is controlled by the mask param , when a bit in he mask is set so the opposite bit
 *           in the register can be changed using the value in the value param.
 *           If the bit in the mask is cleared , the opposite bit in the register remains unchanged.
 *
 */
static inline uint32_t HW_SET_REG32(uint32_t reg,
									uint32_t value,
									uint32_t mask);
									
/* ========================================================================== */
/*                           Static Function Definitions                      */
/* ========================================================================== */
static inline uint32_t HW_RD_REG32(uint32_t reg)
{
	//uint32_t regVal = (*((volatile uint32_t *) addr)) ;
	//return (*((volatile uint32_t *) addr)) ;
	return reg;
}

static inline uint32_t HW_WR_REG32(uint32_t reg,uint32_t value )
{
	//uint32_t regVal = (*((volatile uint32_t *) addr)) ;
	//(*((volatile uint32_t *) addr)) = value ;
	reg = value ;
	return 0;
}

static inline void HW_SET_BIT(uint32_t reg,
								     uint32_t bit)
{
	reg |= (1UL<<bit);
}

static inline void HW_CLEAR_BIT(uint32_t reg,
								     uint32_t bit)
{
	reg &= ~(1UL<<bit);
}

static inline void HW_TOGGLE_BIT(uint32_t reg,
								     uint32_t bit)
{
	reg ^= (1UL<<bit);
}

static inline uint32_t HW_READ_BIT(uint32_t reg,
								       uint32_t bit)
{
	//return ((reg >> bit) & 1U);
	return reg &((1UL<<bit)>>bit) ;
}



static inline uint32_t HW_SET_REG32(uint32_t reg,uint32_t value , uint32_t mask )
{
	//uint32_t regVal = (*((volatile uint32_t *) addr)) ;
	reg &= ~(mask);
	reg |=  value ;
	return 0;
}



#endif

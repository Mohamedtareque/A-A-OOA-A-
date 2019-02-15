/**
 * \file    types.h
 *
 * \brief   This file defines the basic data types used to fixed length types.
 *          Currently the standard types defined in stdint.h are used. This
 *          file also contains macros defining the TRUE,FALSE and NULLi pointer
 *          values.
 *
 *  \date   feb 13, 2019
 *  \author Kotoz
 */

#ifndef TYPES_H_
#define TYPES_H_

/* ========================================================================== */
/*                           Macros & Typedefs                                */
/* ========================================================================== */
typedef enum generalstatus
{
	LOW ,
	HIGH
}gpioGeneralStatus_t;

typedef enum boolean
{
	FASLE = 0 , TRUE ,
	false = 0 , true ,
}boolean_t;


/** \brief Defines TRUE status value */
#ifndef TRUE
#define TRUE     (1U)
#endif

/** \brief Defines FALSE status value */
#ifndef FALSE
#define FALSE    (0U)
#endif

/** \brief Defines NULL pointer value */
#ifndef NULL
#define NULL ((void*) 0U)
#endif

/** \brief create a 32 bit unsigned type */
typedef unsigned int uint32_t;

/** \brief create a 8 bit unsigned type */
typedef unsigned char uint8_t;

/** \brief create a 16 bit unsigned type */
typedef unsigned short uint16_t;



#endif /* TYPES_H_ */

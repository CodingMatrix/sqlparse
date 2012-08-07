'''
Created on 07/08/2012

@author: piranna
'''
from difflib  import ndiff
from unittest import main, TestCase

from sqlparse import format


class Issue_73(TestCase):
    maxDiff = None

    original_raw = ("update JOBINFORMATION set EXTERNALBONUSAMOUNT=0.0, "
    "EXTERNALBONUS=0, INTERNALBONUSAMOUNT=0.0, INTERNALBONUS=0, "
    "SOURCINGBUDGET=NULL, TRAVELCOSTS=NULL, RELOCATIONCOSTS=NULL, "
    "OTHERCOSTS=NULL, ADDITIONALINFORMATION=NULL, "
    "CREATIONDATE=TO_TIMESTAMP('2012-08-06 10:21:00.0', 'YYYY-MM-DD HH24:MI:SS.FF'), "
    "LASTMODIFIEDDATE=TO_TIMESTAMP('2012-08-06 10:24:02.940000000', 'YYYY-MM-DD HH24:MI:SS.FF'), "
    "JOBGRADE=NULL, MIDPOINTSALARY=NULL, ISEXPENSEREIMBURSABLE=0, "
    "REQUESTEDBILLRATE=NULL, HIGHQUARTILESALARY=NULL, LOWQUARTILESALARY=NULL, "
    "AUTOREJECTCANDIDATES=1, AUTODECLINECANDIDATES=1, ESTIMATEDEXPENSE=NULL, "
    "ESTIMATEDLABORCOST=NULL, ESTIMATEDTOTALBUDGET=0.0, "
    "BILLRATENOTTOEXCEED=NULL, BILLRATEMEDIAN=NULL, "
    "CREATIONFLOWTYPEDIMENSIONNO=16, NBTOHIRE=1, UNLIMITEDHIRE=0, "
    "VALIDITYPERIODENABLED=0, VALIDITYPERIOD=NULL, AUTOPOOLINGENABLED=0, "
    "RCAUTOPOOLINGCRITERIANO=NULL, GROUPNO=0, BONUSRSCURRENCYNO=1, "
    "CONTINGENTCURRENCYNO=NULL, BUDGETRSCURRENCYNO=1, CITIZENSHIPSTATUSNO=1, "
    "CSWWORKFLOWNO=11060, EMPLOYEESTATUSNO=1, JOBFIELDNO=130000, "
    "JOBSCHEDULENO=1, JOBSHIFTNO=1, JOBTYPENO=1, STRUCTURENO=1, HIRETYPENO=1, "
    "PRIMARYLOCATIONNO=1038, PROGRAMNO=NULL, CREATOROPERATORNO=17656, "
    "RECRUITEROWNEROPERATORNO=17656, STUDYLEVELNO=NULL, WILLTRAVELNO=NULL, "
    "OFFERNO=19086, METAPRESCREENINGFORMNO=16331, JOBLEVELNO=NULL, "
    "OVERTIMESTATUSNO=NULL, JOBROLENO=NULL, EMPEQUITYESTABLISHMENTNO=NULL "
    "where JOBINFORMATIONNO=16256;")

    def assertMultiLineEqual(self, first, second, msg=None):
        """Assert that two multi-line strings are equal.

        If they aren't, show a nice diff.

        """
        self.assertTrue(isinstance(first, basestring),
                'First argument is not a string')
        self.assertTrue(isinstance(second, basestring),
                'Second argument is not a string')

        if first != second:
            message = ''.join(ndiff(first.splitlines(True),
                                    second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("Multi-line strings are unequal:\n" + message)

    def test_format(self):
        result = format(self.original_raw, reindent=True)

        expected = """update JOBINFORMATION
set EXTERNALBONUSAMOUNT = 0.0,
    EXTERNALBONUS = 0,
    INTERNALBONUSAMOUNT = 0.0,
    INTERNALBONUS = 0,
    SOURCINGBUDGET = NULL,
    TRAVELCOSTS = NULL,
    RELOCATIONCOSTS = NULL,
    OTHERCOSTS = NULL,
    ADDITIONALINFORMATION = NULL,
    CREATIONDATE = TO_TIMESTAMP('2012-08-06 10:21:00.0',
                                'YYYY-MM-DD HH24:MI:SS.FF'),
    LASTMODIFIEDDATE = TO_TIMESTAMP('2012-08-06 10:24:02.940000000',
                                    'YYYY-MM-DD HH24:MI:SS.FF'),
    JOBGRADE = NULL,
    MIDPOINTSALARY = NULL,
    ISEXPENSEREIMBURSABLE = 0,
    REQUESTEDBILLRATE = NULL,
    HIGHQUARTILESALARY = NULL,
    LOWQUARTILESALARY = NULL,
    AUTOREJECTCANDIDATES = 1,
    AUTODECLINECANDIDATES = 1,
    ESTIMATEDEXPENSE = NULL,
    ESTIMATEDLABORCOST = NULL,
    ESTIMATEDTOTALBUDGET = 0.0,
    BILLRATENOTTOEXCEED = NULL,
    BILLRATEMEDIAN = NULL,
    CREATIONFLOWTYPEDIMENSIONNO = 16,
    NBTOHIRE = 1,
    UNLIMITEDHIRE = 0,
    VALIDITYPERIODENABLED = 0,
    VALIDITYPERIOD = NULL,
    AUTOPOOLINGENABLED = 0,
    RCAUTOPOOLINGCRITERIANO = NULL,
    GROUPNO = 0,
    BONUSRSCURRENCYNO = 1,
    CONTINGENTCURRENCYNO = NULL,
    BUDGETRSCURRENCYNO = 1,
    CITIZENSHIPSTATUSNO = 1,
    CSWWORKFLOWNO = 11060,
    EMPLOYEESTATUSNO = 1,
    JOBFIELDNO = 130000,
    JOBSCHEDULENO = 1,
    JOBSHIFTNO = 1,
    JOBTYPENO = 1,
    STRUCTURENO = 1,
    HIRETYPENO = 1,
    PRIMARYLOCATIONNO = 1038,
    PROGRAMNO = NULL,
    CREATOROPERATORNO = 17656,
    RECRUITEROWNEROPERATORNO = 17656,
    STUDYLEVELNO = NULL,
    WILLTRAVELNO = NULL,
    OFFERNO = 19086,
    METAPRESCREENINGFORMNO = 16331,
    JOBLEVELNO = NULL,
    OVERTIMESTATUSNO = NULL,
    JOBROLENO = NULL,
    EMPEQUITYESTABLISHMENTNO = NULL
where JOBINFORMATIONNO = 16256;"""

        self.assertMultiLineEqual(result, expected)

    def test_allign_identifierslist(self):
        result = format(self.original_raw, reindent=True)

        expected = """update JOBINFORMATION
set EXTERNALBONUSAMOUNT         = 0.0,
    EXTERNALBONUS               = 0,
    INTERNALBONUSAMOUNT         = 0.0,
    INTERNALBONUS               = 0,
    SOURCINGBUDGET              = NULL,
    TRAVELCOSTS                 = NULL,
    RELOCATIONCOSTS             = NULL,
    OTHERCOSTS                  = NULL,
    ADDITIONALINFORMATION       = NULL,
    CREATIONDATE                = TO_TIMESTAMP('2012-08-06 10:21:00.0',
                                               'YYYY-MM-DD HH24:MI:SS.FF'),
    LASTMODIFIEDDATE            = TO_TIMESTAMP('2012-08-06 10:24:02.940000000',
                                               'YYYY-MM-DD HH24:MI:SS.FF'),
    JOBGRADE                    = NULL,
    MIDPOINTSALARY              = NULL,
    ISEXPENSEREIMBURSABLE       = 0,
    REQUESTEDBILLRATE           = NULL,
    HIGHQUARTILESALARY          = NULL,
    LOWQUARTILESALARY           = NULL,
    AUTOREJECTCANDIDATES        = 1,
    AUTODECLINECANDIDATES       = 1,
    ESTIMATEDEXPENSE            = NULL,
    ESTIMATEDLABORCOST          = NULL,
    ESTIMATEDTOTALBUDGET        = 0.0,
    BILLRATENOTTOEXCEED         = NULL,
    BILLRATEMEDIAN              = NULL,
    CREATIONFLOWTYPEDIMENSIONNO = 16,
    NBTOHIRE                    = 1,
    UNLIMITEDHIRE               = 0,
    VALIDITYPERIODENABLED       = 0,
    VALIDITYPERIOD              = NULL,
    AUTOPOOLINGENABLED          = 0,
    RCAUTOPOOLINGCRITERIANO     = NULL,
    GROUPNO                     = 0,
    BONUSRSCURRENCYNO           = 1,
    CONTINGENTCURRENCYNO        = NULL,
    BUDGETRSCURRENCYNO          = 1,
    CITIZENSHIPSTATUSNO         = 1,
    CSWWORKFLOWNO               = 11060,
    EMPLOYEESTATUSNO            = 1,
    JOBFIELDNO                  = 130000,
    JOBSCHEDULENO               = 1,
    JOBSHIFTNO                  = 1,
    JOBTYPENO                   = 1,
    STRUCTURENO                 = 1,
    HIRETYPENO                  = 1,
    PRIMARYLOCATIONNO           = 1038,
    PROGRAMNO                   = NULL,
    CREATOROPERATORNO           = 17656,
    RECRUITEROWNEROPERATORNO    = 17656,
    STUDYLEVELNO                = NULL,
    WILLTRAVELNO                = NULL,
    OFFERNO                     = 19086,
    METAPRESCREENINGFORMNO      = 16331,
    JOBLEVELNO                  = NULL,
    OVERTIMESTATUSNO            = NULL,
    JOBROLENO                   = NULL,
    EMPEQUITYESTABLISHMENTNO    = NULL
where JOBINFORMATIONNO = 16256;"""

        self.assertMultiLineEqual(result, expected)

    def test_full(self):
        result = format(self.original_raw, reindent=True)

        expected = """update JOBINFORMATION
   set EXTERNALBONUSAMOUNT         = 0.0,
       EXTERNALBONUS               = 0,
       INTERNALBONUSAMOUNT         = 0.0,
       INTERNALBONUS               = 0,
       SOURCINGBUDGET              = NULL,
       TRAVELCOSTS                 = NULL,
       RELOCATIONCOSTS             = NULL,
       OTHERCOSTS                  = NULL,
       ADDITIONALINFORMATION       = NULL,
       CREATIONDATE                = TO_TIMESTAMP('2012-08-06 10:21:00.0',
                                                  'YYYY-MM-DD HH24:MI:SS.FF'),
       LASTMODIFIEDDATE            = TO_TIMESTAMP('2012-08-06 10:24:02.940000000',
                                                  'YYYY-MM-DD HH24:MI:SS.FF'),
       JOBGRADE                    = NULL,
       MIDPOINTSALARY              = NULL,
       ISEXPENSEREIMBURSABLE       = 0,
       REQUESTEDBILLRATE           = NULL,
       HIGHQUARTILESALARY          = NULL,
       LOWQUARTILESALARY           = NULL,
       AUTOREJECTCANDIDATES        = 1,
       AUTODECLINECANDIDATES       = 1,
       ESTIMATEDEXPENSE            = NULL,
       ESTIMATEDLABORCOST          = NULL,
       ESTIMATEDTOTALBUDGET        = 0.0,
       BILLRATENOTTOEXCEED         = NULL,
       BILLRATEMEDIAN              = NULL,
       CREATIONFLOWTYPEDIMENSIONNO = 16,
       NBTOHIRE                    = 1,
       UNLIMITEDHIRE               = 0,
       VALIDITYPERIODENABLED       = 0,
       VALIDITYPERIOD              = NULL,
       AUTOPOOLINGENABLED          = 0,
       RCAUTOPOOLINGCRITERIANO     = NULL,
       GROUPNO                     = 0,
       BONUSRSCURRENCYNO           = 1,
       CONTINGENTCURRENCYNO        = NULL,
       BUDGETRSCURRENCYNO          = 1,
       CITIZENSHIPSTATUSNO         = 1,
       CSWWORKFLOWNO               = 11060,
       EMPLOYEESTATUSNO            = 1,
       JOBFIELDNO                  = 130000,
       JOBSCHEDULENO               = 1,
       JOBSHIFTNO                  = 1,
       JOBTYPENO                   = 1,
       STRUCTURENO                 = 1,
       HIRETYPENO                  = 1,
       PRIMARYLOCATIONNO           = 1038,
       PROGRAMNO                   = NULL,
       CREATOROPERATORNO           = 17656,
       RECRUITEROWNEROPERATORNO    = 17656,
       STUDYLEVELNO                = NULL,
       WILLTRAVELNO                = NULL,
       OFFERNO                     = 19086,
       METAPRESCREENINGFORMNO      = 16331,
       JOBLEVELNO                  = NULL,
       OVERTIMESTATUSNO            = NULL,
       JOBROLENO                   = NULL,
       EMPEQUITYESTABLISHMENTNO    = NULL
 where JOBINFORMATIONNO = 16256;"""

        self.assertMultiLineEqual(result, expected)


if __name__ == "__main__":
    main()

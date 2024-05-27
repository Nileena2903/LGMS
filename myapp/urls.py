
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('logout/',views.logout),


# ADMIN MODULE
    path('adminHome/', views.adminHome),
    path('adminHome1/', views.adminHome1),

# department
    path('addDept/',views.addDept),
    path('viewDepartment/',views.viewDepartment),
    path('viewDepartment_post/', views.viewDepartment_post),
    path('addDept_post/',views.addDept_post),
    path('editDept/<id>',views.editDept),
    path('editDept_post/',views.editDept_post),
    path('deleteDept/<id>',views.deleteDept),
# staff
    path('addstaff/',views.addstaff),
    path('viewStaff/',views.viewStaff),
    path('viewStaff_post/',views.viewStaff_post),
    path('addstaff_post/',views.addstaff_post),
    path('editStaff/<id>', views.editStaff),
    path('editStaff_post/', views.editStaff_post),
    path('deleteStaff/<id>', views.deleteStaff),
# ward
    path('addWard/',views.addWard),
    path('addWard_post/',views.addWard_post),
    path('viewWard/',views.viewWard),
    path('viewWard_post/',views.viewWard_post),
    path('deleteWard/<id>',views.deleteWard),
    path('editWard/<id>',views.editWard),
    path('editWard_post/',views.editWard_post),



# wardmember
    path('addWardmember/',views.addWardmember),
    path('addWardmember_post/', views.addWardmember_post),
    path('viewWardmember/',views.viewWardmember),
    path('viewWardmember_post/',views.viewWardmember_post),
    path('editWardmember/<id>', views.editWardmember),
    path('editWardmember_post/', views.editWardmember_post),
    path('deleteWardmember/<id>', views.deleteWardmember),

# user
    path('viewUser/', views.viewUser),
    path('viewUser_post/', views.viewUser_post),
    path('GetWard/', views.GetWard),
    path('UserViewServices/', views.UserViewServices),


    # certificate

    path('addCertificate/',views.addCertificate),
    path('addCertificate_post/',views.addCertificate_post),
    path('viewCertificate/',views.viewCertificate),
    path('viewCertificate_post/',views.viewCertificate_post),
    path('editCertificate/<id>',views.editCertificate),
    path('editCertificate_post/',views.editCertificate_post),
    path('deleteCertificate/<id>',views.deleteCertificate),
    path('admin_viewBirthapplications/<id>',views.admin_viewBirthapplications),
    path('admin_viewBirthapplications_post/',views.admin_viewBirthapplications_post),
    path('admin_approveBirthCertificate/<id>',views.admin_approveBirthCertificate),
    path('admin_viewBirthdetails/<id>',views.admin_viewBirthdetails),
    path('admin_approveCertificate/<id>',views.admin_approveCertificate),

# scheme
    path('addScheme/', views.addScheme),
    path('addScheme_post/', views.addScheme_post),
    path('viewScheme/',views.viewScheme),
    path('viewScheme_post/',views.viewScheme_post),
    path('editScheme/<id>', views.editScheme),
    path('editScheme_post/', views.editScheme_post),
    path('deleteScheme/<id>',views.deleteScheme),
    path('admin_viewjobcardapplications/<id>',views.admin_viewjobcardapplications),
    path('admin_viewjobcardapplications_post/',views.admin_viewjobcardapplications_post),
    path('admin_viewjobcarddetails/<id>',views.admin_viewjobcarddetails),
    path('admin_approvejobcard/<id>',views.admin_approvejobcard),
    path('admin_rejectjobcard/<id>',views.admin_rejectjobcard),


# plans
    path('addPlans/', views.addPlans),
    path('addPlans_post/', views.addPlans_post),
    path('viewPlans/',views.viewPlans),
    path('viewPlans_post/',views.viewPlans_post),
    path('editPlans/<id>', views.editPlans),
    path('editPlans_post/', views.editPlans_post),
    path('deletePlans/<id>',views.deletePlans),
    path('admin_viewPlanReq/',views.admin_viewPlanReq),
    path('admin_approvePlanReq/<id>',views.admin_approvePlanReq),
    path('admin_viewApprovedPlans/',views.admin_viewApprovedPlans),

# STAFF MODULE

path('staffHome/',views.staffHome),
path('staffProfile/',views.staffProfile),
path('staffviewScheme/',views.staffviewScheme),
path('staffviewScheme_post/',views.staffviewScheme_post),
path('staffviewCertificate/',views.staffviewCertificate),
path('staffviewCertificate_post/',views.staffviewCertificate_post),
path('viewjobcardapplications/',views.viewjobcardapplications),
path('viewjobcardapplications_post/',views.viewjobcardapplications_post),
path('rejectjobcard/<id>',views.rejectjobcard),
path('viewjobcarddetails/<id>',views.viewjobcarddetails),
path('viewjobcarddetails_post/',views.viewjobcarddetails_post),
path('viewjobcards/<id>',views.viewjobcards),
path('staff_verifyjobcard/<id>',views.staff_verifyjobcard),
path('viewEmployeemateApplication/',views.viewEmployeemateApplication),
path('viewEmployeemates/',views.viewEmployeemates),
path('viewEmployeemates_post/',views.viewEmployeemates_post),
path('verifyEmployeemateApplication/<id>',views.verifyEmployeemateApplication),
path('rejectEmpmateReq/<id>',views.rejectEmpmateReq),
path('deleteEmpmate/<id>',views.deleteEmpmate),

path('rejecteddstaffviewworkreqapply_post/',views.rejecteddstaffviewworkreqapply_post),
path('approvedstaffviewworkreqapply_post/',views.approvedstaffviewworkreqapply_post),
path('staffviewworkreqapply_post/',views.staffviewworkreqapply_post),
path('rejecteddstaffviewworkreqapply/',views.rejecteddstaffviewworkreqapply),
path('approvedstaffviewworkreqapply/<id>',views.approvedstaffviewworkreqapply),
path('staffviewworkreqapply/',views.staffviewworkreqapply),
path('approveworkreq/<id>',views.approveworkreq),
path('rejectworkreq/<id>',views.rejectworkreq),
path('staff_viewworkrequest/<id>',views.staff_viewworkrequest),
# path('staff_viewworkrequest/',views.staff_viewworkrequest),
path('staff_viewworkrequestverified/',views.staff_viewworkrequestverified),
path('staff_viewdistinctwrkrequest/',views.staff_viewdistinctwrkrequest),
path('staff_viewemployeesreq/<id>',views.staff_viewemployeesreq),
path('staff_approvewrkrequest/<id>',views.staff_approvewrkrequest),
path('viewBirthapplications/<id>',views.viewBirthapplications),
path('viewBirthapplications_post/',views.viewBirthapplications_post),
path('viewBirthdetails/<id>',views.viewBirthdetails),
path('staff_verifyBirthapplications/<id>',views.staff_verifyBirthapplications),
path('staff_rejectBirthapplications/<id>',views.staff_rejectBirthapplications),

# WARDMEMBER MODULE

path('memberHome/',views.memberHome),
path('memberProfile/',views.memberProfile),
path('verifyUser/',views.verifyUser),
path('verifyUser_post/', views.verifyUser_post),
path('approve/<id>',views.approve),
path('reject/<id>',views.reject),
path('acceptedUser/',views.acceptedUser),
path('acceptedUser_post/',views.acceptedUser_post),
path('viewWardPlans/',views.viewWardPlans),
path('viewWardPlans_post/',views.viewWardPlans_post),
path('sendPlanReq/<id>',views.sendPlanReq),
path('sendPlanReq_post/',views.sendPlanReq_post),
path('sendPlanNotification/<id>',views.sendPlanNotification),
path('sendPlanNotification_post/',views.sendPlanNotification_post),



#USER MODULE

    path('user_signup/',views.user_signup),
    path('user_login/',views.user_login),
    path('viewProfile/',views.viewProfile),
    path('editProfile/',views.editProfile),
    path('UserViewServices/',views.UserViewServices),
    path('BirthRegister/',views.BirthRegister),
    path('DeathRegister/',views.DeathRegister),

    path('UserViewSchemes/',views.UserViewSchemes),
    path('jobcard/',views.jobcard),
    path('viewJobcardDetails/',views.viewJobcardDetails),
    path('addmembers/',views.addmembers),
    path('Viewmembers/',views.Viewmembers),
    path('sendEmployeematereq/',views.sendEmployeematereq),
    path('UserViewNotifications/',views.UserViewNotifications),
    path('useraddapplyworkreq/',views.useraddapplyworkreq),
    path('viewmycertificates/',views.viewmycertificates),
    path('user_view_allocation/',views.user_view_allocation),
    path('view_my_attendance/',views.view_my_attendance),


#EMPLOYEEMATE MODULE
    path('viewEmployeemateProfile/', views.viewEmployeemateProfile),
    path('employeemateviewpublishlist/', views.employeemateviewpublishlist),
    path('markattendance/', views.markattendance),
    path('emp_add_attendance/', views.emp_add_attendance),
    path('workallocation/<id>', views.workallocation),
    path('workallocationpost/', views.workallocationpost),
    path('employeemateviewworkrequest/', views.employeemateviewworkrequest),
    path('employeematefoewardtostaff/', views.employeematefoewardtostaff),
    path('employeemateviewallocatedarea/', views.employeematefoewardtostaff),
    path('employeemateviewcalculation/', views.employeemateaddworkallocation),
    path('employeematedeletewrkrequest/', views.employeematedeletewrkrequest),
    path('viewassignedworkers/', views.viewassignedworkers),
    path('emp_add_allocation/', views.emp_add_allocation),
    path('usersendworkrequest/', views.usersendworkrequest),
    path('staff_viewattendance/<id>', views.staff_viewattendance),
    path('userviewworkhistory/', views.userviewworkhistory),

]

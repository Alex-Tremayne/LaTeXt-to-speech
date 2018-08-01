
math_subs = {
	'+':' plus ',
	'-':' minus ',
	'\pm':' plus or minus ',
	'\times':' times ',
	'$':'',#Not sure about this, should probably use to check for math mode, but will suffice for now
	'_':' subscript ',
	'^':' to the power of '
	}

greek_subs = {
	'\alpha':' alpha ',
	'\beta':' beta ',
	'\gamma':' gamma ',
	'\delta':' delta ',
	'\epsilon':' epsilon ',
	'\zeta':' zeta ',
	'\eta':' eta ',
	'\theta':' theta ',
	'\iota':' iota ',
	'\kappa':' kappa ',
	'\lambda':' lambda ',
	'\mu':' mu ',
	'\nu':' nu ',
	'\\xi':' xi ',
	'\omicron':' omicron ',
	'\pi': ' pi ',
	'\rho':' rho ',
	'\sigma': ' sigma ',
	'\tau':' tau ',
	'\\upsilon':' upsilon ',
	'\phi':' phi ',
	'\chi':' chi ',
	'\psi':' psi ',
	'\omega':' omega ',
	'\Alpha':' big alpha ',
	'\Beta':' big beta ',
	'\Gamma':' big gamma ',
	'\Delta':' big delta ',
	'\Epsilon':' big epsilon ',
	'\Zeta':' big zeta ',
	'\Eta':' big eta ',
	'\Theta':' big theta ',
	'\Iota':' big iota ',
	'\Kappa':' big kappa ',
	'\Lambda':' big lambda ',
	'\Mu':' big mu ',
	'\\Nu':' big nu ',
	'\\Xi':' big xi ',
	'\Omicron':' big omicron ',
	'\Pi': ' big pi ',
	'\Rho':' big rho ',
	'\Sigma': ' big sigma ',
	'\Tau':' big tau ',
	'\\Upsilon':' big upsilon ',
	'\Phi':' big phi ',
	'\Chi':' big chi ',
	'\Psi':' big psi ',
	'\Omega':' big omega '
}

misc_sym_subs = {
	'\odot':' oh dot ',
	'\oplus':' oh plus ',
	'\ominus':' oh minus'
}


astro_subs = {
	'M_\odot':' solar masses ',
	'M{\odot}':' solar masses ',
	'R_\odot':' solar radii ',
	'R_{\odot}':' solar radii '
}


def latex_to_text(input, user_subs="", astro_sub=False):

	text = input

	if astro_subs:
		for key in astro_subs:
			text = text.strip()
			text = text.replace(key, astro_subs[key])

	
	for key in math_subs:
		text = text.strip()
		text = text.replace(key, math_subs[key])

	for key in greek_subs:
		text = text.strip()
		text = text.replace(key, greek_subs[key])

	for key in misc_sym_subs:
		text = text.strip()
		text = text.replace(key, misc_sym_subs[key])

	return text
